[![validate_badge](https://github.com/muppet3000/homeassistant-grott/actions/workflows/validate.yml/badge.svg)](https://github.com/muppet3000/homeassistant-grott/actions)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?logo=homeassistantcommunitystore)](https://github.com/hacs/integration)
[![bmab_badge](https://img.shields.io/badge/Buy_Me-A_Beer-FFDD00.svg?logo=buymeacoffee)](https://www.buymeacoffee.com/muppet3000)
[![paypal_badge](https://img.shields.io/badge/PayPal-Beer_Fund-blue.svg?&logo=paypal)](https://www.paypal.com/paypalme/muppet3000)

# WORK IN PROGRESS - DO NOT USE!!!!

# Grott Home Assistant Custom Component (grott)
Custom component (installable via HACS) for registering sensors associated with Growatt inverters that are being published via [Grott](https://github.com/johanmeijer/grott).
See [prerequisites](docs/prerequisites.md) for more information.

# Installation
This integration can be installed via HACS for Home Assistant
1. [Install HACS](https://hacs.xyz/docs/setup/prerequisites) (Follow all the way through to the 'Configuration' page)
1. In HACS install this integration:
    1. Click 'HACS' on the left menu
    1. Click 'Integrations'
    1. Click the three dots in the top-right corner
    1. Click 'Custom repositories'
    1. In the 'Repository' field enter: `https://github.com/muppet3000/homeassistant-grott`
    1. In the 'Category' field select 'Integration'
    1. Click 'Add'
    1. Once the repository is added click on `Grott`
    1. On the next page select 'Download' in the bottom-right corner
    1. Choose the latest released version and click 'DOWNLOAD'
    1. Click the 'HACS' button in the menu and restart Home Assistant when prompted
    <!-- THIS WILL WORK WHEN IT'S IN THE DEFAULT REPOS
    1. Click 'Explore & Download Repositories'
    1. Search for 'Grott' & click it
    1. Click 'Download' and follow on-screen instructions
    -->
1. Once the plugin is installed via HACS configure it just like a normal Home Assistant Integration i.e. from Settings -> Devices & Settings -> Add Integration -> Search for Grott

or (if you don't want to use HACS)

1. Download the latest release to your custom_components folder inside the Home Assistant configuration directory and unpack it

# Implementation
On initial release this plugin works in read-only mode and pulls data from an MQTT server that has been pushed to by Grott (more information/how to configure this [here](docs/prerequisites.md))

The future plan will be to grow this project so that it allows configuration of inverters via Grott also.

# More Info
- [Prerequisites](docs/prerequisites.md)
- [FAQ](docs/FAQ.md)
