# In progress
- Change "calc_values" to a CONST
- Doesn't re-load config on restart, even though the config appears to show that it has
  - Does now, but there must be a better way of handling 'options' and 'config' rather than having them duplicated


# Essential
- Calculated values
- Options to choose whether to include calculated values
- Option to choose the MQTT topic - see here for how to allow it as an option (need to unsubscribe and then re-subscribe): https://github.com/home-assistant/core/blob/dev/homeassistant/components/mqtt/client.py#L153-L163
- README file
  - Pre-requisites
  - How to setup grott
  - How to setup MQTT in HA

# Future
- Pushing config to Grott server

# Nice to Have
- Handle restarts - load last value??
