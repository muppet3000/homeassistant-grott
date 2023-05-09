# Setup - HomeAssistant MQTT Broker
The Home Assistant MQTT broker is the simplest part of the whole system, it simply allows Home Assistant to know where the MQTT server is running so that it can register and listen for updates.

## Configuration
1. In HomeAssistant navigate to the Integrations page (`Settings` -> `Devices & Services`)

<kbd>![image](https://github.com/muppet3000/homeassistant-grott/assets/10612068/f6e4f4b1-f0c0-409d-bec5-a3a5620da0ed)</kbd>

2. Click `Add Integration`

<kbd>![image](https://github.com/muppet3000/homeassistant-grott/assets/10612068/f0975b56-c326-4ab4-b22a-f4203479855f)</kbd>

3. Type `MQTT` and select the Integration

<kbd>![image](https://github.com/muppet3000/homeassistant-grott/assets/10612068/785d799b-b9f2-41bf-9ed8-b83d843610fb)</kbd>


4. Select `MQTT` from the options that appear

<kbd>![image](https://github.com/muppet3000/homeassistant-grott/assets/10612068/6aa56df5-8f21-4c15-90d4-94fdd0bfe23b)</kbd>

5. In the configuration enter the hostname/IP of the "Broker" that was setup running MQTT

<kbd>![image](https://github.com/muppet3000/homeassistant-grott/assets/10612068/90dba7eb-9b48-473f-abcc-c4463df160eb)</kbd>

6. Enter `1883` in the Port (See above)
7. Leave all other fields blank and click `Next`
8. For all other setup options use the default values

# Summary
You now have completed all of the prequisite steps in order to use Grott to forward data to Home Assistant.
If you haven't already installed the HomeAssistant Grott Integration, follow the steps [here](README.md) and then data should start appearing within a minute.

Further information on how the setup works & further setup steps, take a look at the [FAQ](FAQ.md).
