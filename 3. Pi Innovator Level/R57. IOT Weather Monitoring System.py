"""
IoT Weather Monitoring System with Blynk
- Displays temperature and humidity on Blynk radial gauges
"""

import time
import adafruit_dht
import RPi.GPIO as GPIO
from BlynkLib import Blynk  # Import Blynk library

# Blynk Authentication Token (Replace with your Blynk Token)
BLYNK_AUTH = 'YOUR_BLYNK_AUTH_TOKEN'

# Initialize Blynk
blynk = Blynk(BLYNK_AUTH)

# Define GPIO Pin for DHT11 Sensor
DHT_PIN = 17  # Data pin connected to GPIO17

# Initialize DHT Sensor
dht_sensor = adafruit_dht.DHT11(DHT_PIN)

try:
    while True:
        try:
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

        except Exception as e:
            print(f"Error: {e}")

        blynk.run()  # Process Blynk data
        time.sleep(2)  # Update every 2 seconds

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()  # Clean up GPIO settings
