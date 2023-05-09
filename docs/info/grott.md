# Grott
Grott works as a proxy between your datalogger and the growatt servers which host data. It intercepts the data, decodes it and then forwards it to endpoints of your choosing before forwarding the original packets on to Growatt.

## Default setup
The following diagram illustrates (very primitively) how a default Growatt setup works
<kbd>![growatt-grott-diagrams drawio (1)](https://github.com/muppet3000/homeassistant-grott/assets/10612068/ccaf9634-d21c-40ea-8160-052760dc3b84)</kbd>

## Grott setup
The following diagram illustrates how Grott is introduced to divert data to additional endpoints
<kbd>![growatt-grott-diagrams drawio (2)](https://github.com/muppet3000/homeassistant-grott/assets/10612068/3607ac46-4b18-43cc-8b6e-faa6df10414f)</kbd>
