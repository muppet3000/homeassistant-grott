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

from grott.const import (
    BATTERY_TYPES
)

def battery_type_lookup(mqtt_data):
  batt_type=mqtt_data['values']['batterytype']
  if batt_type > 1:
    batt_type = 2
  return BATTERY_TYPES[int(batt_type)]

SENSORS_MQTT = [
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
    "name": "Time Since Commissioned",
    "device_class": SensorDeviceClass.DURATION,
    "unit_of_measurement": UnitOfTime.HOURS,
    "state_class": SensorStateClass.TOTAL,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:clock",
    "func": lambda js: js['values']["totworktime"],
    "divider": 7200
  },
 
  {
    "name": "Generated Energy (eactoday) ??? - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["eactoday"],
    "divider": 10
  },
  {
    "name": "Generated Energy (pvenergytoday) ??? - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["pvenergytoday"],
    "divider": 10
  },
  {
    "name": "Generated Energy (eactotal) ??? - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["eactotal"],
    "divider": 10
  },

  {
    "name": "PV1 Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv1today"],
    "divider": 10
  },
  {
    "name": "PV1 Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv1total"],
    "divider": 10
  },
  {
    "name": "PV2 Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv2today"],
    "divider": 10
  },
  {
    "name": "PV2 Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epv2total"],
    "divider": 10
  },
  {
    "name": "All PV Energy (epvtotal)??? - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["epvtotal"],
    "divider": 10
  },

  {
    "name": "Inverter Temperature",
    "device_class": SensorDeviceClass.TEMPERATURE,
    "unit_of_measurement": UnitOfTemperature.CELSIUS,
    "state_class": SensorStateClass.MEASUREMENT,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:thermometer",
    "func": lambda js: js['values']["pvtemperature"],
    "divider": 10
  },
  {
    "name": "IPM Temperature",
    "device_class": SensorDeviceClass.TEMPERATURE,
    "unit_of_measurement": UnitOfTemperature.CELSIUS,
    "state_class": SensorStateClass.MEASUREMENT,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:thermometer",
    "func": lambda js: js['values']["pvipmtemperature"],
    "divider": 10
  },
  {
    "name": "Boost Temperature",
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
    "name": "AC Charge Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["eacharge_today"],
    "divider": 10
  },
  {
    "name": "AC Charge Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:solar-power",
    "func": lambda js: js['values']["eacharge_total"],
    "divider": 10
  },

  {
    "name": "Battery Type",
    "device_class": SensorDeviceClass.ENUM,
    "options": BATTERY_TYPES,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": battery_type_lookup
  },

  #TODO - Convert to an ENUM
  #0x00:waiting module 
  #0x01: Self-test mode,
  #      optional
  #0x02: Reserved
  #0x03：SysFault module 
  #0x04: Flash module
  #0x05：PVBATOnline module, 
  #0x06：BatOnline module 
  #0x07：PVOfflineMode module, 
  #0x08：BatOfflineMode module,
  {
    "name": "System Work Mode",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["uwsysworkmode"],
  },


  {
    "name": "System Fault Word 0",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword0"],
  },
  {
    "name": "System Fault Word 1",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword1"],
  },
  {
    "name": "System Fault Word 2",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword2"],
  },
  {
    "name": "System Fault Word 3",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword3"],
  },
  {
    "name": "System Fault Word 4",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword4"],
  },
  {
    "name": "System Fault Word 5",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword5"],
  },
  {
    "name": "System Fault Word 6",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword6"],
  },
  {
    "name": "System Fault Word 7",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["systemfaultword7"],
  },

  {
    "name": "Battery Discharging Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:battery-arrow-down",
    "func": lambda js: js['values']["pdischarge1"],
    "divider": 10
  },
  {
    "name": "Battery Charging Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:battery-arrow-up",
    "func": lambda js: js['values']["p1charge1"],
    "divider": 10
  },
  {
    "name": "Battery Voltage",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-battery",
    "func": lambda js: js['values']["vbat"],
    "divider": 10
  },
  {
    "name": "Statement of Charge",
    "device_class": SensorDeviceClass.BATTERY,
    "unit_of_measurement": PERCENTAGE,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-battery",
    "func": lambda js: js['values']["SOC"],
    "divider": 1
  },

  {
    "name": "Import from Grid Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-import-outline",
    "func": lambda js: js['values']["pactouserr"],
    "divider": 10
  },
#  {
#    "name": "Import from Grid Power - All",
#    "device_class": SensorDeviceClass.POWER,
#    "unit_of_measurement": UnitOfPower.WATT,
#    "state_class": SensorStateClass.MEASUREMENT,
#    "icon": "mdi:home-import-outline",
#    "func": lambda js: js['values']["pactousertot"],
#    "divider": 10
#  },

  {
    "name": "Export to Grid Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-export-outline",
    "func": lambda js: js['values']["pactogridr"],
    "divider": 10
  },
#  {
#    "name": "Export to Grid Power - All",
#    "device_class": SensorDeviceClass.POWER,
#    "unit_of_measurement": UnitOfPower.WATT,
#    "state_class": SensorStateClass.MEASUREMENT,
#    "icon": "mdi:home-export-outline",
#    "func": lambda js: js['values']["pactogridtot"],
#    "divider": 10
#  },

  {
    "name": "Load Consumption Power",
    "device_class": SensorDeviceClass.POWER,
    "unit_of_measurement": UnitOfPower.WATT,
    "state_class": SensorStateClass.MEASUREMENT,
    "icon": "mdi:home-lightning-bolt",
    "func": lambda js: js['values']["plocaloadr"],
    "divider": 10
  },
#  {
#    "name": "Load Consumption Power - All",
#    "device_class": SensorDeviceClass.POWER,
#    "unit_of_measurement": UnitOfPower.WATT,
#    "state_class": SensorStateClass.MEASUREMENT,
#    "icon": "mdi:home-lightning-bolt",
#    "func": lambda js: js['values']["plocaloadtot"],
#    "divider": 10
#  },


  #TODO - This might be an enum
  {
    "name": "SP State",
    "device_class": None,
    "unit_of_measurement": None,
    "state_class": None,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:information-outline",
    "func": lambda js: js['values']["spdspstatus"],
  },

  {
    "name": "SP Bus Voltage",
    "device_class": SensorDeviceClass.VOLTAGE,
    "unit_of_measurement": UnitOfElectricPotential.VOLT,
    "state_class": SensorStateClass.MEASUREMENT,
    "entity_category": EntityCategory.DIAGNOSTIC,
    "icon": "mdi:flash",
    "func": lambda js: js['values']["spbusvolt"],
    "divider": 10
  },

  {
    "name": "Import from Grid Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:home-import-outline",
    "func": lambda js: js['values']["etouser_tod"],
    "divider": 10
  },
  {
    "name": "Import from Grid Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:home-import-outline",
    "func": lambda js: js['values']["etouser_tot"],
    "divider": 10
  },
  {
    "name": "Export to Grid Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:home-export-outline",
    "func": lambda js: js['values']["etogrid_tod"],
    "divider": 10
  },
  {
    "name": "Export to Grid Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:home-import-outline",
    "func": lambda js: js['values']["etogrid_tot"],
    "divider": 10
  },

  {
    "name": "Battery Discharged Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:battery-arrow-down",
    "func": lambda js: js['values']["edischarge1_tod"],
    "divider": 10
  },
  {
    "name": "Battery Discharged Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:battery-arrow-down",
    "func": lambda js: js['values']["edischarge1_tot"],
    "divider": 10
  },

  {
    "name": "Battery Charged Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:battery-arrow-up",
    "func": lambda js: js['values']["eharge1_tod"],
    "divider": 10
  },
  {
    "name": "Battery Charged Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:battery-arrow-up",
    "func": lambda js: js['values']["eharge1_tot"],
    "divider": 10
  },

  {
    "name": "Load Consumption Energy - Today",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL_INCREASING,
    "icon": "mdi:home-lightning-bolt",
    "func": lambda js: js['values']["elocalload_tod"],
    "divider": 10
  },
  {
    "name": "Load Consumption Energy - Total",
    "device_class": SensorDeviceClass.ENERGY,
    "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
    "state_class": SensorStateClass.TOTAL,
    "icon": "mdi:home-lightning-bolt",
    "func": lambda js: js['values']["elocalload_tot"],
    "divider": 10
  },
]


