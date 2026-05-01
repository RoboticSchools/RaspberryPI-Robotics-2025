"""
Components Used:
1. Raspberry Pi
2. DHT11 Sensor (Temperature & Humidity)
3. Blynk Web App
4. Jumper Wires

Install Required Libraries:
pip3 install adafruit-circuitpython-dht adafruit-blinka --break-system-packages
pip3 install blynk-library-python --break-system-packages
"""

import time
import adafruit_dht
import RPi.GPIO as gpio
from BlynkLib import Blynk
import board

# ---------------- Blynk Setup ----------------
BLYNK_AUTH = 'your_blynk_auth_token'  # Replace with your Blynk auth token
blynk = Blynk(BLYNK_AUTH, server="blynk.cloud", port=80)

# ---------------- GPIO Setup ----------------
gpio.setmode(gpio.BCM)  # Use BCM numbering

# ---------------- Sensor Setup ----------------
dht_sensor = adafruit_dht.DHT11(board.D17)  # DHT11 connected to GPIO17

# ---------------- Main Loop ----------------
try:
    while True:
        try:
            # Read temperature and humidity from DHT11
            temperature = dht_sensor.temperature
            humidity = dht_sensor.humidity

            # Check if readings are valid
            if temperature is not None and humidity is not None:
                print(f"Temperature: {temperature} C, Humidity: {humidity}%")

                # Send values to Blynk app
                blynk.virtual_write(1, temperature)  # V1 → Temperature
                blynk.virtual_write(2, humidity)     # V2 → Humidity
            else:
                print("Sensor Error")

        except RuntimeError as error:
            # Handle DHT timing errors
            print("Read error:", error)

        blynk.run()     # Maintain Blynk connection
        time.sleep(2)   # Delay between readings

except KeyboardInterrupt:
    # Clean exit
    print("Exiting...")
    gpio.cleanup()