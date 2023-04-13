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
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv1today"] + js['values']['epv2today'],
    "divider": 10,
    "unique_name": "calculated_001",
  },

  {
    "name": "PV-All Energy - Total (Calculated)",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv1total"] + js['values']['epv2total'],
    "divider": 10,
    "unique_name": "calculated_002",
  },

  {
    "name": "Load Consumption Energy (AC) - Today (Calculated)",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:home-lightning-bolt",
    #Import from Grid - Battery AC Charge
    "func": lambda js: js['values']["etouser_tod"] - js['values']['eacharge_today'],
    "divider": 10,
    "unique_name": "calculated_003",
  },

  {
    "name": "Load Consumption Energy (PV) - Today (Calculated)",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:home-lightning-bolt",
    #Load Consumption - Load Consumption AC - Battery Discharged
    "func": lambda js: js['values']["elocalload_tod"] - (js['values']["etouser_tod"] - js['values']['eacharge_today']) - js['values']['edischarge1_tod'],
    "divider": 10,
    "unique_name": "calculated_004",
  },

  {
    "name": "Load Consumption Energy (PV + Battery) - Today (Calculated)",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:home-lightning-bolt",
    #Load Consumption - Load Consumption AC
    "func": lambda js: js['values']["elocalload_tod"] - (js['values']["etouser_tod"] - js['values']['eacharge_today']),
    "divider": 10,
    "unique_name": "calculated_005",
  },

  {
    "name": "System Output (Self-consumption + Export) - Today (Calculated)",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:flash",
    #Load Consumption Energy (PV + Battery) + Export
    "func": lambda js: js['values']["elocalload_tod"] - (js['values']["etouser_tod"] - js['values']['eacharge_today']) + js['values']["etogrid_tod"],
    "divider": 10,
    "unique_name": "calculated_006",
  },
]

