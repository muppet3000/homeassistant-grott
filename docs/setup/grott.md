# Setup - Grott
Grott is the key part of the setup, it is what intercepts the data that would typically flow directly to the Growatt servers and allows it to be diverted to Home Assistant before also forwarding on to the Growatt server website (meaning that the ShinePhone app etc still works). For more information on how Grott works, see a brief overview [here](../info/grott.md).

Grott can be run in 3 ways:
1. Docker
2. Python application
3. [Grott add-on](https://github.com/egguy/ha-addons/tree/main)

How to run all three options are listed below. NOTE - Until you have a valid configuration file from the [configuration](#configuration) section Grott will not start correctly.

## Docker
To run grott as a docker container you can the following command:
```
docker run -d -v <path_to_config_file>:/app/grott.ini -p 5279:5279 ledidobe/grott:2.7.8
```
Where `<path_to_config_file` is replaced with the path locally for your configuration file created in the [configuration](#configuration) section below

See [docker-compose guide](docker-compose-guide.md) for a more complete docker deployment method

## Python Application
Adapted from [here](https://github.com/johanmeijer/grott/wiki/@-First-time-installation).

1. Download the repository from here: https://github.com/johanmeijer/grott
1. Install the dependencies: `sudo pip3 install paho-mqtt requests`
1. Run grott: `python3 grott.py -v` (This won't work because we haven't done the configuration yet)
1. Setup grott to run as a service (just follow [these](https://github.com/johanmeijer/grott/wiki/Grott-as-a-service-(Linux)) instructions)

## Grott add-on 
This add on has a stable and beta branch, read the guidelines over which to use to suit your needs. 

Follow the instructions to install the grott add-on (https://github.com/egguy/ha-addons)

Take note of the specific instructions [here](https://github.com/egguy/addon-grott/blob/main/grott/DOCS.md#compatibility-with-homeassistant-grott) about checking: *Enable grott MQTT* and to deactivate the *Home Assistant plugin* in the configuration. This can lead to duplicate sensors otherwise.

Then you should have a working Grott server running as an add-on to HA and the IP address of the HA instance will be the destination IP address to re-point your datalogger to (see [here](https://github.com/egguy/addon-grott/blob/main/grott/DOCS.md#configuration-of-the-wi-fi-logger))

Then you can proceed to install the grott integration, and ignore the Configuration step below...

# Configuration
These steps provide the most basic configuration file setup for Grott, for more detailed options and configuration breakdown, you can read more detail in the Grott repo itself [here](https://github.com/johanmeijer/grott/wiki/Grott-Configuration).

Copy the configuration file from [here](https://github.com/johanmeijer/grott/blob/master/examples/grott.ini) to a location of your choice (in the case of the Python installation it is expected to be in the same location as the `.py` files themselves.

The default configuration file has no useful configuration, to make things work with Home Assistant the following changes need to be made:
1. In the `Generic` section:
    1. `invtype` - Choose one of `default`,`sph`,`spf`,`max`, `tl3`
1. In the MQTT section:
    1. `ip` - Set to the IP or hostname of the machine that will be running your MQTT server (see [mqtt](mqtt.md) for more information) 
    1. `port` - Set to the port that your MQTT server is running on (default is 1883)
    1. `topic` - Uncomment, defaults to `energy/growatt`
    1. `auth` - Uncomment, defaults to `False`

# Summary
At this point you should now have a running Grott server which is capable of receiving traffic from your inverter and forwarding it to both MQTT AND the Growatt Servers.

Next: [Datalogger Config](datalogger.md)
