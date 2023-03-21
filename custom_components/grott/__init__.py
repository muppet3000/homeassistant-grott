"""The grott component."""
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_DEVICE_ID,
)
from homeassistant.core import HomeAssistant

from .const import(
    CONF_CALC_VALUES,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor"]

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Grott integration."""

    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}
    
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    _LOGGER.debug("Setting up Grott integration")

    if entry.entry_id not in hass.data[DOMAIN]:
        hass.data[DOMAIN][entry.entry_id] = {}

    _LOGGER.debug("Entry data: %s", entry.data)
    _LOGGER.debug("Entry options: %s", entry.options)

    hass.data[DOMAIN][entry.entry_id][CONF_DEVICE_ID] = entry.data[CONF_DEVICE_ID].strip().upper().replace(":", "").replace(" ", "")
    _LOGGER.debug("Target device: %s", hass.data[DOMAIN][entry.entry_id][CONF_DEVICE_ID])

    hass.data[DOMAIN][entry.entry_id][CONF_CALC_VALUES] = entry.data[CONF_CALC_VALUES]
    _LOGGER.debug("Include calculated values: %s", hass.data[DOMAIN][entry.entry_id][CONF_CALC_VALUES])

    for component in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, component))

    entry.async_on_unload(entry.add_update_listener(async_update_listener))

    _LOGGER.debug("Finished setting up Grott integration")
    return True


async def async_update_listener(hass: HomeAssistant, entry: ConfigEntry):
    """Handle options update."""
    _LOGGER.debug("Updated options receieved: %s", entry.options)
    hass.data[DOMAIN][entry.entry_id][CONF_DEVICE_ID] = entry.options[CONF_DEVICE_ID].strip().upper().replace(":", "").replace(" ", "")
    hass.data[DOMAIN][entry.entry_id][CONF_CALC_VALUES] = entry.options[CONF_CALC_VALUES]
    hass.config_entries.async_update_entry(entry, data=entry.options)
    _LOGGER.debug("Finished handling updated options")
