# FAQ
This page is intended to answer questions associated with the Grott Integration, not Grott (although the Grott documentation is lacking, so there are some helpers in this repo) or Home Assistant itself.

#### Table of Contents
- [How does Grott actually work?](#how-does-grott-actually-work)
- [How can I use Grott but keep my old sensor names from the growatt-server-api integration?](#how-can-i-use-grott-but-keep-my-old-sensor-names-from-the-growatt-server-api-integration)

## How does Grott actually work?
See [here](info/grott.md)

## How can I use Grott but keep my old sensor names from the growatt-server-api integration?
Short answer: Use template sensors to copy the values provided by grott but use the same names as the previous growatt-server-api sensors.
Long answer: I've created a set of example entries to be placed in the `configuration.yaml` file for HomeAssistant [here](../examples/templates/template_configuration.yaml), feel free to copy & tweak accordingly. 
1. Replace `<DEVICE_ID-UPPER_CASE>` with the upper-case version of your inverter's device ID e.g. `NWCPA40001`
2. Replace `<DEVICE_ID-LOWER_CASE>` with the lower-case version of your inverter's device ID e.g. `nwcpa40001`
