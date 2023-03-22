"""Sensor descriptions for Growatt systems - Raw MQTT values."""

from __future__ import annotations
from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import (
    PERCENTAGE,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfFrequency,
    UnitOfPower,
    UnitOfTemperature,
    UnitOfTime,
)
from homeassistant.helpers.entity import DeviceInfo, EntityCategory

SENSORS_LABEL="calculated_sensors"

SENSORS = [
  {
    "name": "PV-All Energy - Today (Calculated)",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv1today"] + js['values']['epv2today'],
    "divider": 10
  },

  {
    "name": "PV-All Energy - Total (Calculated)",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv1total"] + js['values']['epv2total'],
    "divider": 10
  },

  #TODO - More values to add here from Spreadsheet
]

