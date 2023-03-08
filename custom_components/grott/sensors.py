"""Sensor descriptions for Growatt systems."""

from __future__ import annotations
from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import (
    PERCENTAGE,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfPower,
)
from homeassistant.helpers.entity import DeviceInfo, EntityCategory

SENSORS = [
  {
    "name": "PV Serial",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["pvserial"],
  },
  {
    "name": "Datalog Serial",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["datalogserial"],
  },
  {
    "name": "PV Status",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["pvstatus"],
  },
  {
    "name": "PV Power - All",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pvpowerin"],
    "divider": 10
  },
  {
    "name": "PV1 Voltage",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv1voltage"],
    "divider": 10
  },
  {
    "name": "PV1 Current",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv1current"],
    "divider": 10
  },
  {
    "name": "PV1 Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv1watt"],
    "divider": 10
  },
  {
    "name": "PV2 Voltage",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv2voltage"],
    "divider": 10
  },
  {
    "name": "PV2 Current",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv2current"],
    "divider": 10
  },
  {
    "name": "PV2 Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pv2watt"],
    "divider": 10
  },

  {
    "name": "Statement of charge",
    "device_class": SensorDeviceClass.BATTERY,
    "unit_of_measurement": PERCENTAGE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-battery",
    "func": lambda js: js['values']["SOC"],
    "divider": 1
  },



  {
    "name": "Load Consumption",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["plocaloadr"],
    "divider": 10
  },

]


