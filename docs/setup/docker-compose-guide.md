# Docker Compose Guide
This is a condensed version of what I use myself, docker simplifies the whole process and nicely compartmentalises installation of dependencies etc. I even use it to run Home Assistant.

## Setup
1. Install docker & docker-compose (if you've come this far, you know how to use Google)
2. Copy the docker-compose directory from examples in this repo (download all the files): [here](../../examples/docker-compose)
3. Change into the directory
4. Run `docker-compose up -d` or if you want to run it in foreground mode and be swamped by output: `docker-compose up`

## Extra steps
Even when using docker-compose to simplify things, you still need to follow the manual steps of the setup process:
1. [Inverter/DataLogger Config](datalogger.md)
2. [Home Assistant MQTT Broker](homeassistant-mqtt-broker.md)

## More notes
Within the `docker-compose.yml` file is also a commented out setup of Home Assistant. You don't have to use it, it's just there as an example.
