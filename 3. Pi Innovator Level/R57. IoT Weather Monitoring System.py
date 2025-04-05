"""
Components Used:
- Raspberry Pi
- DHT11 Temperature and Humidity Sensor
- Blynk App (with Virtual Pins V1 and V2)
- Jumper Wires
"""

import time
import adafruit_dht
import RPi.GPIO as GPIO
from BlynkLib import Blynk  # Import Blynk library

# Blynk Authentication Token (Replace with your Blynk Token)
blynk_auth = 'YOUR_BLYNK_AUTH_TOKEN'

# Initialize Blynk
blynk = Blynk(blynk_auth)

# Define GPIO Pin for DHT11 Sensor
dht_pin = 17  # Data pin connected to GPIO17

# Initialize DHT Sensor
dht_sensor = adafruit_dht.DHT11(dht_pin)

try:
    while True:
        # Read Temperature and Humidity
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity

        if temperature is not None and humidity is not None:
            print(f"Temperature: {temperature}°C, Humidity: {humidity}%")

            # Send Data to Blynk Dashboard
            blynk.virtual_write(1, temperature)  # Send Temperature to Virtual Pin V1
            blynk.virtual_write(2, humidity)     # Send Humidity to Virtual Pin V2
        else:
            print("Failed to read sensor data.")

        blynk.run()  # Process Blynk data
        time.sleep(2)  # Update every 2 seconds

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()  # Clean up GPIO settings
