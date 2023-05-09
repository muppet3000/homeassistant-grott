# Setup - MQTT
MQTT is used as a broker/intermediary for the data leaving Grott. Grott pushes the data to MQTT then Home Assistant registers with the MQTT service to be notified whenever new data is available. You can read a lot more about MQTT [here](https://mqtt.org/).
For the purposes of this setup, you can just use the most basic configuration, outlined below.

MQTT can be set up in a variety of ways, below outlines 2 potential options:
1. Docker
2. Local install

## Docker
To run MQTT as a docker container you can the following command:
```
docker run -d -v <path_to_mqtt_dir>/config:/mosquitto/config -v <path_to_mqtt_dir>/data:/mosquitto/data -v <path_to_mqtt_dir>/log:/mosquitto/log -p 1883:1883 eclipse-mosquitto
```
Where `<path_to_mqtt_dir>` is replaced with the path locally for a directory to store anything persistent e.g. configuration files and data, please see the [configuration](#configuration) section below for what should appear in the configuration file

See [docker-compose guide](docs/setup/docker-compose-guide.md) for a more complete docker deployment method

## Local install
Install relevant version from this page: https://www.mosquitto.org/download/

Installation instructions should be included with their respective binaries

# Configuration
MQTT requires the most basic of configurations in order to work with Grott.

A configuration file (`<path_to_mqtt_dir>/config/mosquitto.conf`) should be created with the following contents:
```
allow_anonymous true
listener 1883
persistence true
persistence_location /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log
```
NOTE: This assumes the default path for the docker container, replace with the path to your MQTT installation if you followed the [Local install](#LocalInstall) steps

# Summary
At this point you should now have a running Grott server and a running MQTT instance, Grott should already be forwarding data to MQTT if you configured the correct `ip` and `port` in the [grott setup](grott.md)

Next: [HomeAssistant MQTT Broker](homeassistant-mqtt-broker.md)
