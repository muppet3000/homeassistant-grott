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
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.helpers.entity import DeviceInfo, EntityCategory
from .const import DOMAIN
from .sensors import SENSORS
from homeassistant.const import (
    CONF_DEVICE_ID,
    ATTR_DEVICE_ID,
)
from homeassistant.core import callback
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.util import slugify

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Grott sensors."""

    # the config is defaulted to + which happens to mean we will subscribe to all devices
    device = hass.data[DOMAIN][config_entry.entry_id][CONF_DEVICE_ID]

    device_update_groups = {}

    @callback
    async def mqtt_message_received(message: ReceiveMessage):
        """Handle received MQTT message."""
        topic = message.topic
        payload = json.loads(message.payload)
        _LOGGER.debug("Received message: %s", topic)
        _LOGGER.debug("  Payload: %s", payload)


#home-assistant-test    | 2023-03-01 21:32:34.534 DEBUG (MainThread) [custom_components.grott.sensor] Received message: energy/growatt
#home-assistant-test    | 2023-03-01 21:32:34.535 DEBUG (MainThread) [custom_components.grott.sensor]   Payload: {"device": "NWCPA47006", "time": "2023-03-01T21:32:34", "buffered": "no", "values": {"datalogserial": "NAC3915162", "pvserial": "NWCPA47006", "pvstatus": 6, "pvpowerin": 0, "pv1voltage": 123, "pv1current": 0, "pv1watt": 1, "pv2voltage": 0, "pv2current": 0, "pv2watt": 0, "pvpowerout": 0, "pvfrequentie": 5000, "pvgridvoltage": 2464, "pvgridcurrent": 15, "pvgridpower": 0, "pvgridvoltage2": 0, "pvgridcurrent2": 0, "pvgridpower2": 0, "pvgridvoltage3": 0, "pvgridcurrent3": 0, "pvgridpower3": 0, "totworktime": 111688551, "eactoday": 120, "pvenergytoday": 120, "eactotal": 138743, "epvtotal": 107934, "epv1today": 25, "epv1total": 60803, "epv2today": 16, "epv2total": 32732, "pvtemperature": 232, "pvipmtemperature": 223, "pvboosttemp": 213, "bat_dsp": 522, "eacharge_today": 95, "eacharge_total": 46348, "batterytype": 1, "uwsysworkmode": 6, "systemfaultword0": 0, "systemfaultword1": 0, "systemfaultword2": 0, "systemfaultword3": 0, "systemfaultword4": 32, "systemfaultword5": 0, "systemfaultword6": 0, "systemfaultword7": 2048, "pdischarge1": 0, "p1charge1": 0, "vbat": 519, "SOC": 11, "pactouserr": 12707, "pactousertot": 12707, "pactogridr": 0, "pactogridtot": 0, "plocaloadr": 12700, "plocaloadtot": 12700, "spdspstatus": 6, "spbusvolt": 2957, "etouser_tod": 206, "etouser_tot": 115836, "etogrid_tod": 2, "etogrid_tot": 297107, "edischarge1_tod": 101, "edischarge1_tot": 67936, "eharge1_tod": 88, "eharge1_tot": 63816, "elocalload_tod": 260, "elocalload_tot": 4294898079}}


#{"device": "NWCPA47006", "time": "2023-03-01T21:30:32", "buffered": "no", "values": {"datalogserial": "NAC3915162", "pvserial": "NWCPA47006", "pvstatus": 6, "pvpowerin": 0, "pv1voltage": 118, "pv1current": 0, "pv1watt": 1, "pv2voltage": 0, "pv2current": 0, "pv2watt": 0, "pvpowerout": 0, "pvfrequentie": 5002, "pvgridvoltage": 2462, "pvgridcurrent": 15, "pvgridpower": 0, "pvgridvoltage2": 0, "pvgridcurrent2": 0, "pvgridpower2": 0, "pvgridvoltage3": 0, "pvgridcurrent3": 0, "pvgridpower3": 0, "totworktime": 111688278, "eactoday": 120, "pvenergytoday": 120, "eactotal": 138743, "epvtotal": 107934, "epv1today": 25, "epv1total": 60803, "epv2today": 16, "epv2total": 32732, "pvtemperature": 234, "pvipmtemperature": 225, "pvboosttemp": 214, "bat_dsp": 521, "eacharge_today": 95, "eacharge_total": 46348, "batterytype": 1, "uwsysworkmode": 6, "systemfaultword0": 0, "systemfaultword1": 0, "systemfaultword2": 0, "systemfaultword3": 0, "systemfaultword4": 32, "systemfaultword5": 0, "systemfaultword6": 0, "systemfaultword7": 2048, "pdischarge1": 0, "p1charge1": 0, "vbat": 518, "SOC": 11, "pactouserr": 12462, "pactousertot": 12462, "pactogridr": 0, "pactogridtot": 0, "plocaloadr": 12400, "plocaloadtot": 12400, "spdspstatus": 6, "spbusvolt": 2953, "etouser_tod": 206, "etouser_tot": 115836, "etogrid_tod": 2, "etogrid_tot": 297107, "edischarge1_tod": 101, "edischarge1_tot": 67936, "eharge1_tod": 88, "eharge1_tot": 63816, "elocalload_tod": 260, "elocalload_tot": 4294898079}}


#        for thing in payload:
#            _LOGGER.debug(thing)
        device_id = payload["device"]
#       device_id = topic.split("/")[1]
        if (device == '+' or device_id == device):
            update_groups = await async_get_device_groups(device_update_groups, async_add_entities, device_id)
#            _LOGGER.debug("Received message: %s", topic)
#            _LOGGER.debug("  Payload: %s", payload)
            for update_group in update_groups:
                update_group.process_update(message)






    data_topic = "energy/growatt/#"

    await mqtt.async_subscribe(
        hass, data_topic, mqtt_message_received, 1
    ) 



async def async_get_device_groups(device_update_groups, async_add_entities, device_id):
    #Add to update groups if not already there
    if device_id not in device_update_groups:
        _LOGGER.debug("New device found: %s", device_id)
        groups = [
            GrottSensorUpdateGroup(device_id, SENSORS),
        ]
        async_add_entities(
            [sensorEntity for updateGroup in groups for sensorEntity in updateGroup.all_sensors],
            #True
        )
        device_update_groups[device_id] = groups

    return device_update_groups[device_id]
  

class GrottSensorUpdateGroup:
    """Representation of Grott Sensors that all get updated together."""

    def __init__(self, device_id: str, sensors: Iterable) -> None:
        """Initialize the sensor collection."""
        self._device_id = device_id
        self._sensors = [GrottSensor(device_id = device_id, **sensor) for sensor in sensors]

    def process_update(self, message: ReceiveMessage) -> None:
        """Process an update from the MQTT broker."""
        topic = message.topic
        payload = json.loads(message.payload)
        if (self._device_id == payload['device']):
            _LOGGER.debug("Matched on %s", self._device_id)
            #for value in payload['values']: 
            #    _LOGGER.debug(value)
#            parsed_data = json.loads(payload)
            for sensor in self._sensors:
                sensor.process_update(payload)

    @property
    def all_sensors(self) -> Iterable[GrottSensor]:
        """Return all meters."""
        return self._sensors

class GrottSensor(SensorEntity):
    """Representation of a sensor that is updated via MQTT."""

    def __init__(self, device_id, name, icon, device_class, unit_of_measurement = None, state_class = None, func = None, divider = None, entity_category = None, ignore_zero_values = False, options = None) -> None:
        """Initialize the sensor."""
        self._device_id = device_id
        self._ignore_zero_values = ignore_zero_values
        self._attr_name = name
        self._attr_unique_id = slugify(device_id + "_" + name)
        self._attr_icon = icon
        self._attr_device_class = device_class
        self._attr_native_unit_of_measurement = unit_of_measurement
        self._attr_state_class = state_class
        self._attr_entity_category = entity_category
        self._attr_options = options
        self._attr_should_poll = False
        
        self._func = func        
        self._divider = divider
        self._attr_device_info = DeviceInfo(
            connections={("Inverter", device_id)},
            manufacturer="Growatt",
            model="Grott MQTT",
            name=f"Inverter {device_id}",
        )
        self._attr_native_value = None

    def process_update(self, mqtt_data) -> None:
        """Update the state of the sensor."""
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
        return {ATTR_DEVICE_ID: self._device_id}
