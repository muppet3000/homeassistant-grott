# Setup - Inverter/Data Logger Configuration
In order for Grott to intercept the data you must re-configure your ShineLink box or dongle to ship data to Grott rather than directly to the Growatt servers.

The instructions on this site describe the process for a ShineLan Box and ShineWiFi-X/S.

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

## ShineWiFi-X/S Re-configuration

To reconfigure your ShineWiFi-X/S datalogger, you need to use the ShinePhone app and have your datalogger already added to your plant. (This guide and photos are based on Android.)

1. **Start the ShinePhone App:**  
   Go to `Me` and select `Datalogger Configuration`.  
   <kbd><img src="https://github.com/user-attachments/assets/b28d743a-232f-4bf7-85b3-0cde6e67886f" height="400"/></kbd>

2. **Add the Datalogger:**  
   Scan the QR Code on the ShineWiFi-X/S dongle or manually enter the serial number and verification code, then click `Confirm`.  
   <kbd><img src="https://github.com/user-attachments/assets/3b0dce79-2018-4f99-b5d9-622ee64ac1b1" height="400"/></kbd>
   <kbd><img src="https://github.com/user-attachments/assets/23918dfc-6230-452f-9cfe-7a3177e73d2c" height="400"/></kbd>
   <kbd><img src="https://github.com/user-attachments/assets/03b5ec4c-9aab-4adc-9969-e94644744f1d" height="400"/></kbd>

3. **Select Hotspot Mode:**  
   <kbd><img src="https://github.com/user-attachments/assets/0944f11b-a337-4780-81ea-4b6a8d494f80" height="400"/></kbd>

4. **Activate Hotspot Mode:**  
   Press the datalogger button to enter `Hotspot Mode`. Ensure the `blue LED` on the datalogger is always on. Then select `Next Step`.  
   <kbd><img src="https://github.com/user-attachments/assets/6a6b7386-d809-4715-b2dc-333cff5205b1" height="400"/></kbd>
   <kbd><img src="https://github.com/user-attachments/assets/b664e5c2-8eaf-4afc-8bf9-ce4029b87360" height="400"/></kbd>

5. **Connect to Datalogger's WiFi:**  
   Connect your mobile phone to the WiFi network with the same name as the `SN` of the datalogger. Go back to the app and select `Next Step`.  
   <kbd><img src="https://github.com/user-attachments/assets/05b2e4cf-d80e-4593-ba62-132bd3ef7d67" height="400"/></kbd>
   <kbd><img src="https://github.com/user-attachments/assets/a21d1e30-eba2-4e9d-819d-bc2407de969b" height="400"/></kbd>

6. **View Current WiFi:**  
   The app will display the current WiFi network the datalogger is connected to. Select `Advanced`.  
   <br>
   <kbd><img src="https://github.com/user-attachments/assets/fa02cdfb-a397-4c22-baa3-cd2572717b9b" height="400"/></kbd>

7. **Adjust Server Settings:**  
   Select `Server Settings`, then select it again. Enter the password in the following format: `growattYYYYMMDD`, and press `Unlock`.  
   <kbd><img src="https://github.com/user-attachments/assets/b12c5241-3eca-42dc-85ce-6c18ce8a1c79" height="400"/></kbd>
   <kbd><img src="https://github.com/user-attachments/assets/fe48cd65-3996-491e-9325-82db4f918475" height="400"/></kbd>

8. **Configure Server IP:**  
   Uncheck `Set the domain name`, then enter the IP address of the machine running the Grott application/service into the `Server IP` field. Press `Save` and return to `Datalogger Configuration`.  
   <kbd><img src="https://github.com/user-attachments/assets/1e491a4a-84fa-4ddc-b678-5378f83a9a80" height="400"/></kbd>

9. **Finalize Configuration:**  
   Select `Configure Immediately` wait 1-2 min and your done.  
   <kbd><img src="https://github.com/user-attachments/assets/0721da90-1e09-4d2a-928e-7d1986b519b6" height="400"/></kbd>

# Summary
At this point you should now have your inverter sending data to Grott which should also forward the data on to the Growatt Servers and also ready to forward to MQTT

Next: [MQTT](mqtt.md)
