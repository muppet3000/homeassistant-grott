# Setup - Grott
Grott is the key part of the setup, it is what intercepts the data that would typically flow directly to the Growatt servers and allows it to be diverted to Home Assistant before also forwarding on to the Growatt server website (meaning that the ShinePhone app etc still works). For more information on how Grott works, see a brief overview [here](docs/info/grott.md).

Grott can be run in 2 ways:
1. Docker
2. Python application

How to run both options are listed below.

## Docker
To run grott as a docker container you can the following command:
```
docker run -d -v <path_to_config_file>:/app/grott.ini -p 5279:5279 ledidobe/grott:2.7.8
```
Where `<path_to_config_file` is replaced with the path locally for your configuration file created in the [configuration](#configuration) section below

See [docker-compose guide](docs/setup/docker-compose-guide.md) for a more complete docker deployment method

## Python Application

# Configuration
