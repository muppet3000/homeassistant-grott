"""Sensor descriptions for Growatt systems."""

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

from .const import (
    BATTERY_TYPES
)

def battery_type_lookup(mqtt_data):
  batt_type=mqtt_data['values']['batterytype']
  if batt_type > 1:
    batt_type = 2
  return BATTERY_TYPES[int(batt_type)]

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
    "name": "Output Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvpowerout"],
    "divider": 10
  },

  {
    "name": "Grid Frequency",
    "device_class": SensorDeviceClass.FREQUENCY,
    "unit_of_measurement": UnitOfFrequency.HERTZ,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:sine-wave",
    "func": lambda js: js['values']["pvfrequentie"],
    "divider": 100
  },

  {
    "name": "Grid Voltage (Single/First Phase)",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridvoltage"],
    "divider": 10
  },
  {
    "name": "Grid Current (Single/First Phase)",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridcurrent"],
    "divider": 10
  },
  {
    "name": "Grid Power??? (Single/First Phase)",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridpower"],
    "divider": 10
  },
  {
    "name": "Grid Voltage (Second Phase)",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridvoltage2"],
    "divider": 10
  },
  {
    "name": "Grid Current (Second Phase)",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridcurrent2"],
    "divider": 10
  },
  {
    "name": "Grid Power??? (Second Phase)",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridpower2"],
    "divider": 10
  },
  {
    "name": "Grid Voltage (Third Phase)",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridvoltage3"],
    "divider": 10
  },
  {
    "name": "Grid Current (Third Phase)",
    "device_class": SensorDeviceClass.CURRENT,
    "unit_of_measurement": UnitOfElectricCurrent.AMPERE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridcurrent3"],
    "divider": 10
  },
  {
    "name": "Grid Power??? (Third Phase)",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["pvgridpower3"],
    "divider": 10
  },

  {
    "name": "Time since commissioned",
    "device_class": SensorDeviceClass.DURATION,
    "unit_of_measurement": UnitOfTime.HOURS,
    "state_class": SensorStateClass.TOTAL,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:clock",
    "func": lambda js: js['values']["totworktime"],
    "divider": 7200
  },
 
  {
    "name": "Today - Generated energy (eactoday) ???",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["eactoday"],
    "divider": 10
  },
  {
    "name": "Today - Generated energy (pvenergytoday) ???",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pvenergytoday"],
    "divider": 10
  },
  {
    "name": "Total - Generated energy (eactotal) ???",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["eactotal"],
    "divider": 10
  },

  {
    "name": "Today - PV1 energy",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv1today"],
    "divider": 10
  },
  {
    "name": "Total - PV1 energy",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv1total"],
    "divider": 10
  },
  {
    "name": "Today - PV2 energy",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv2today"],
    "divider": 10
  },
  {
    "name": "Total - PV2 energy",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv2total"],
    "divider": 10
  },
  {
    "name": "Total - All PV energy (epvtotal)???",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epvtotal"],
    "divider": 10
  },

  {
    "name": "Inverter temperature",
    "device_class": SensorDeviceClass.TEMPERATURE,
    "unit_of_measurement": UnitOfTemperature.CELSIUS,
    "state_class": SensorStateClass.MEASUREMENT,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:thermometer",
    "func": lambda js: js['values']["pvtemperature"],
    "divider": 10
  },
  {
    "name": "IPM temperature",
    "device_class": SensorDeviceClass.TEMPERATURE,
    "unit_of_measurement": UnitOfTemperature.CELSIUS,
    "state_class": SensorStateClass.MEASUREMENT,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:thermometer",
    "func": lambda js: js['values']["pvipmtemperature"],
    "divider": 10
  },
  {
    "name": "Boost temperature",
    "device_class": SensorDeviceClass.TEMPERATURE,
    "unit_of_measurement": UnitOfTemperature.CELSIUS,
    "state_class": SensorStateClass.MEASUREMENT,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:thermometer",
    "func": lambda js: js['values']["pvboosttemp"],
    "divider": 10
  },
  {
    "name": "Bat DSP",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["bat_dsp"],
    "divider": 10
  },

  {
    "name": "Today - AC Charge energy",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["eacharge_today"],
    "divider": 10
  },
  {
    "name": "Total - AC Charge energy",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["eacharge_total"],
    "divider": 10
  },

  {
    "name": "Battery type",
    "device_class": SensorDeviceClass.ENUM,
    "options": BATTERY_TYPES,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:solar-power",
    "func": battery_type_lookup
  },

#  """
#  TODO - Add all of these
#  -  uwsysworkmode        :  6
#  -  systemfaultword0     :  0
#  -  systemfaultword1     :  0
#  -  systemfaultword2     :  0
#  -  systemfaultword3     :  0
#  -  systemfaultword4     :  32
#  -  systemfaultword5     :  0
#  -  systemfaultword6     :  0
#  -  systemfaultword7     :  2048
#  """

  


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


