"""Support for Grott MQTT sensors."""
from __future__ import annotations

import json
import re
import logging
from typing import Iterable

from homeassistant.components import mqtt
from homeassistant.components.mqtt.models import ReceiveMessage
from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.helpers.entity import DeviceInfo, EntityCategory
from .const import DOMAIN, CONF_CALC_VALUES
from .sensors import (
    sensors_calculated,
    sensors_mqtt,
)
from homeassistant.const import (
    CONF_DEVICE_ID,
    ATTR_DEVICE_ID,
)
from homeassistant.core import callback
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.util import slugify

_LOGGER = logging.getLogger(__name__)    

"""Example MQTT message"""
#home-assistant-test    | 2023-03-01 21:32:34.534 DEBUG (MainThread) [custom_components.grott.sensor] Received message: energy/growatt
#home-assistant-test    | 2023-03-01 21:32:34.535 DEBUG (MainThread) [custom_components.grott.sensor]   Payload: {"device": "NWCPA47006", "time": "2023-03-01T21:32:34", "buffered": "no", "values": {"datalogserial": "NAC3915162", "pvserial": "NWCPA47006", "pvstatus": 6, "pvpowerin": 0, "pv1voltage": 123, "pv1current": 0, "pv1watt": 1, "pv2voltage": 0, "pv2current": 0, "pv2watt": 0, "pvpowerout": 0, "pvfrequentie": 5000, "pvgridvoltage": 2464, "pvgridcurrent": 15, "pvgridpower": 0, "pvgridvoltage2": 0, "pvgridcurrent2": 0, "pvgridpower2": 0, "pvgridvoltage3": 0, "pvgridcurrent3": 0, "pvgridpower3": 0, "totworktime": 111688551, "eactoday": 120, "pvenergytoday": 120, "eactotal": 138743, "epvtotal": 107934, "epv1today": 25, "epv1total": 60803, "epv2today": 16, "epv2total": 32732, "pvtemperature": 232, "pvipmtemperature": 223, "pvboosttemp": 213, "bat_dsp": 522, "eacharge_today": 95, "eacharge_total": 46348, "batterytype": 1, "uwsysworkmode": 6, "systemfaultword0": 0, "systemfaultword1": 0, "systemfaultword2": 0, "systemfaultword3": 0, "systemfaultword4": 32, "systemfaultword5": 0, "systemfaultword6": 0, "systemfaultword7": 2048, "pdischarge1": 0, "p1charge1": 0, "vbat": 519, "SOC": 11, "pactouserr": 12707, "pactousertot": 12707, "pactogridr": 0, "pactogridtot": 0, "plocaloadr": 12700, "plocaloadtot": 12700, "spdspstatus": 6, "spbusvolt": 2957, "etouser_tod": 206, "etouser_tot": 115836, "etogrid_tod": 2, "etogrid_tot": 297107, "edischarge1_tod": 101, "edischarge1_tot": 67936, "eharge1_tod": 88, "eharge1_tot": 63816, "elocalload_tod": 260, "elocalload_tot": 4294898079}}


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Grott sensors."""
    device_update_groups = {}
    _LOGGER.info("Configuring sensor using config data & options")

    if config_entry.options:
        _LOGGER.debug("Options found, overwriting config data....")
        hass.config_entries.async_update_entry(config_entry, data=config_entry.options)

    config = {**config_entry.data}
    _LOGGER.debug("Config data: %s", config_entry.data)
    _LOGGER.debug("Config options: %s", config_entry.options)

    @callback
    async def mqtt_message_received(message: ReceiveMessage):
        """Handle received MQTT message."""
        topic = message.topic
        payload = json.loads(message.payload)
        _LOGGER.debug("Received message: %s", topic)
        _LOGGER.debug("Payload: %s", payload)

        # Get the configuration for what device to get data for (defaults to + which means we will subscribe to all devices)
        device = config[CONF_DEVICE_ID]
        _LOGGER.debug("Configured to look for device: %s (+ means all)", device)

        # Get the configuration for whether to include calculated values too
        conf_calc_values = config[CONF_CALC_VALUES]
        _LOGGER.debug("Configured to include calculated values: %s", conf_calc_values)

        device_id = payload["device"]
        if (device == '+' or device_id == device):
            #We cannot handle buffered data, so we ignore it
            if (payload["buffered"] == "no"):
              update_groups = await async_get_device_groups(device_update_groups, async_add_entities, device_id, conf_calc_values, payload)
              for update_group in update_groups:
                  update_group.process_update(payload)
            else:
              _LOGGER.info("Ignoring buffered data encountered from: %s", payload["time"])

        #HACKS START HERE
        #hacked_values={}
        #for key in payload['values']:
        #    if isinstance(payload['values'][key], str):
        #        hacked_values[key] = payload['values'][key]+"4000"
        #    else:
        #        hacked_values[key] = payload['values'][key]+4000
        #_LOGGER.debug(hacked_values)
        #payload['values'] = hacked_values
        #payload['device'] = payload["device"] + "-4000"
        #device_id = payload["device"]
        #if (device == '+' or device_id == device):
        #    update_groups = await async_get_device_groups(device_update_groups, async_add_entities, device_id, conf_calc_values, payload)
        #    for update_group in update_groups:
        #        _LOGGER.debug("Looping update groups")
        #        update_group.process_update(payload)
        #HACKS END HERE


    data_topic = "energy/growatt/#"

    hass.data[DOMAIN][config_entry.entry_id]["unsub_mqtt_listener"] = await mqtt.async_subscribe(
        hass, data_topic, mqtt_message_received, 1
    ) 


async def async_get_device_groups(device_update_groups, async_add_entities, device_id, conf_calc_values, payload):
    #Add to update groups if not already there
    if device_id not in device_update_groups:
        _LOGGER.info("New device found: %s", device_id)
        groups = [
            GrottSensorUpdateGroup(sensors_mqtt.SENSORS_LABEL, device_id, sensors_mqtt.SENSORS, payload),
        ]

        #Only use calculated values if the user has chosen to
        if conf_calc_values:
            groups.append(
                GrottSensorUpdateGroup(sensors_calculated.SENSORS_LABEL, device_id, sensors_calculated.SENSORS, payload),
            )

        async_add_entities(
            [sensorEntity for updateGroup in groups for sensorEntity in updateGroup.all_sensors],
            #True
        )
        device_update_groups[device_id] = groups

    return device_update_groups[device_id]
  
class GrottSensorUpdateGroup:
    """Representation of Grott Sensors that all get updated together."""

    def __init__(self, group_label: str, device_id: str, sensors: Iterable, payload) -> None:
        """Initialize the sensor collection."""
        self._group_label = group_label
        self._device_id = device_id
        self._sensors = []
        for sensor in sensors:
          try:
            value = sensor['func'](payload)
            self._sensors.append(GrottSensor(data_source = group_label, device_id = device_id, **sensor))
          except KeyError:
            _LOGGER.debug("Key Error when attempting to create %s sensor (key may not exist for this system type)", sensor['name'])

    def process_update(self, payload) -> None:
        """Process an update from the MQTT broker."""
        _LOGGER.info("PROCESSING UPDATES")
        _LOGGER.info("%s sensors for processing", len(self._sensors))
        if (self._device_id == payload['device']):
            _LOGGER.debug("%s - matched on %s", self._group_label, self._device_id)
            for sensor in self._sensors:
                sensor.process_update(payload)

    @property
    def all_sensors(self) -> Iterable[GrottSensor]:
        """Return all meters."""
        return self._sensors

class GrottSensor(SensorEntity):
    """Representation of a sensor that is updated via MQTT."""

    def __init__(self, data_source, device_id, name, unique_name, icon, device_class, unit_of_measurement = None, state_class = None, func = None, divider = None, entity_category = None, ignore_zero_values = False, options = None) -> None:
        """Initialize the sensor."""
        self._data_source = data_source 
        self._device_id = device_id
        self._ignore_zero_values = ignore_zero_values
        self._attr_name = f"{device_id} {name}"
        self._attr_unique_id = slugify("grott" + "_" + device_id + "_" + unique_name)
        self._attr_should_poll = False
        
        self._func = func        
        self._divider = divider
        self._attr_device_info = DeviceInfo(
            connections={("Inverter", device_id)},
            manufacturer="Growatt",
            model="Grott MQTT",
            name=f"{device_id}",
            identifiers={(DOMAIN, device_id)}
        )
        self._attr_native_value = None

        description = SensorEntityDescription(
            key=slugify(name),
            name=name,
            device_class=device_class,
            native_unit_of_measurement = unit_of_measurement,
            state_class = state_class,
            icon = icon,
            entity_category = entity_category,
            options = options
        )
        self.entity_description = description

    def process_update(self, mqtt_data) -> None:
        """Update the state of the sensor."""
        _LOGGER.debug("Processing update for: %s, unique id: %s", self._attr_name, self._attr_unique_id)
        new_value = self._func(mqtt_data)
        if self._divider != None:
            new_value = float(new_value)/self._divider
        if (self._ignore_zero_values and new_value == 0):
            _LOGGER.debug("Ignored new value of %s on %s.", new_value, self._attr_unique_id)
            return
        self._attr_native_value = new_value
        if (self.hass is not None): # this is a hack to get around the fact that the entity is not yet initialized at first
            self.async_schedule_update_ha_state()

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return {ATTR_DEVICE_ID: self._device_id, "Data Source": self._data_source}
