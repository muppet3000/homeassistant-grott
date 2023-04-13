"""The grott component."""
import logging
import asyncio

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_DEVICE_ID,
    Platform
)
from homeassistant.core import HomeAssistant

from .const import(
    CONF_CALC_VALUES,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [Platform.SENSOR]

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Grott integration."""

    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}
    
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    _LOGGER.info("Setting up Grott integration")

    if entry.entry_id not in hass.data[DOMAIN]:
        hass.data[DOMAIN][entry.entry_id] = {}

    _LOGGER.debug("Entry data: %s", entry.data)
    _LOGGER.debug("Entry options: %s", entry.options)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(async_update_listener))

    _LOGGER.info("Finished setting up Grott integration")
    return True


async def async_update_listener(hass: HomeAssistant, entry: ConfigEntry):
    """Handle options update."""
    _LOGGER.debug("Updated options receieved: %s, reloading component", entry.options)
    _LOGGER.info("Finished handling updated options, reloading...")
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(
    hass: HomeAssistant, entry: ConfigEntry
) -> bool:
    """Unload a config entry."""
    _LOGGER.info("Unloading...")
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    hass_data = hass.data[DOMAIN]
    # Remove options_update_listener.
    if hass_data[entry.entry_id].get("unsub_mqtt_listener", False):
        _LOGGER.debug("MQTT listener unsub function found, calling it to unsubscribe")
        hass_data[entry.entry_id]["unsub_mqtt_listener"]()

    # Remove config entry from domain.
    if unload_ok:
        hass_data.pop(entry.entry_id)
    _LOGGER.info("Unloading complete")

    return unload_ok
