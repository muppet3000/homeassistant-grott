"""Config flow for Grott."""
import logging

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_DEVICE_ID
from homeassistant.core import callback

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

#TODO - Consider the scenario where the IP of grott is required for push operations

class GrottConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is None:
            return self.async_show_form(
                step_id="user", data_schema=vol.Schema({vol.Required(CONF_DEVICE_ID, default='+'):str}), errors=errors
            )

        device_id = user_input[CONF_DEVICE_ID]

        await self.async_set_unique_id('{}_{}'.format(DOMAIN, device_id))
        self._abort_if_unique_id_configured()

        return self.async_create_entry(
            title="",
            data={CONF_DEVICE_ID: device_id})


    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return GrottOptionsFlowHandler(config_entry)


class GrottOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle a option flow for GrottMQTT."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Handle options flow."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        data_schema=vol.Schema({vol.Required(CONF_DEVICE_ID, default=self.config_entry.options.get(CONF_DEVICE_ID, "+")):str})
        return self.async_show_form(step_id="user", data_schema=data_schema)
