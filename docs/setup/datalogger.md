# Setup - Inverter/Data Logger Configuration
In order for Grott to intercept the data you must re-configure your ShineLink box or dongle to ship data to Grott rather than directly to the Growatt servers.

The instructions on this site describe the process for a ShineLan Box, if anyone can provide information on how to do the same for the Wifi dongle I'll happily update the documentation.

## ShineLan re-configuration
1. You need to know the IP address of your ShineLink/Wifi Dongle, this will vary depending on your home network setup and isn't something I can help you with. 
(Typically looking on your router's configuration or DHCP server you will find something that looks like it.)

1. Once you know its IP address enter it into your browser and you'll find something like this:
<kbd>![image](https://user-images.githubusercontent.com/10612068/212528884-f7d7c44e-6a98-47f7-931c-fc035c3a4f5d.png)</kbd>

1. Enter the credentials (admin/admin by default, or admin/"CC-Code" at the back of your ShineLanBox), and you'll be shown the Datalogger information page, from here click on `Network Setting`:
<kbd>![image](https://user-images.githubusercontent.com/10612068/212528973-f2a5f248-2211-4154-b5aa-f272b5967985.png)</kbd>

1. On the Network Settings page change the `ResolvDomain` to `Off` and the `Server IP` to the IP address of the machine running the Grott application/service.
Before:
<kbd>![image](https://user-images.githubusercontent.com/10612068/235784216-7bd8c2db-324f-4c6c-88a1-b74498f81a5b.png)</kbd>
After:
<kbd>![image](https://user-images.githubusercontent.com/10612068/235784409-ea285e82-86df-45f7-9eee-cda825515955.png)</kbd>

1. OPTIONAL (Increases data frequency) -  On the Network Settings page change the `Data Transfer interval` to one of your choosing (lowest is 1 minute), then click `Save`
<kbd>![image](https://user-images.githubusercontent.com/10612068/212528966-c131c5aa-b478-4753-9648-4d0cbc381169.png)</kbd>

After this your ShineLink/Wifi Dongle will start pushing data to Grott (and optionally more frequently than default also).

# Summary
At this point you should now have your inverter sending data to Grott which should also forward the data on to the Growatt Servers and also ready to forward to MQTT

Next: [MQTT](mqtt.md)
