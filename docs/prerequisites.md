# Prerequisites
In order to make use of the Home Assistant Grott Integration you must first have a working [Grott](https://github.com/johanmeijer/grott) setup. Grott can be configured in many different ways and the Grott repo itself is not particularly helpful in explaining how this can be done. The documentation in this repo aims to simplify/help with the setup process.

Each link below provides a guide on how to setup the relevant components to make data from your inverter appear in Home Assistant, there are plenty of other guides available out there on the internet for each of the services in isolation, however I have pulled together a specific set of documentation here for configuring Grott.

1. [Grott](setup/grott.md)
2. [Inverter/DataLogger Config](setup/datalogger.md)
3. [MQTT](setup/mqtt.md)
4. [Home Assistant MQTT Broker](setup/homeassistant-mqtt-broker.md)

# Alternative setup
For those of you familiar with Docker and/or docker-compose you can configure all of the above with a simple docker-compose.yml file which will bring up the entire stack (including home-assistant as well if you want). You can follow this guide instead: [docker-compose guide](setup/docker-compose-guide.md)
