"""
Components Used:
1. Raspberry Pi
2. DHT11 Temperature and Humidity Sensor
3. Blynk App (Virtual Pins V1 and V2)
4. Jumper Wires
"""

import time
import adafruit_dht
import RPi.GPIO as GPIO
from BlynkLib import Blynk

# ---------------- Blynk Setup ----------------
blynk_auth = 'YOUR_BLYNK_AUTH_TOKEN'  # add your token
blynk = Blynk(blynk_auth)

# ---------------- GPIO Setup ----------------
GPIO.setmode(GPIO.BCM)
dht_pin = 17  # DHT11 data pin

# ---------------- Sensor Setup ----------------
dht_sensor = adafruit_dht.DHT11(dht_pin)

# ---------------- Main Loop ----------------
try:
    while True:
        temperature = dht_sensor.temperature  # read temperature
        humidity = dht_sensor.humidity        # read humidity

        if temperature is not None and humidity is not None:
            print(f"Temperature: {temperature}°C, Humidity: {humidity}%")

            blynk.virtual_write(1, temperature)  # send temp to V1
            blynk.virtual_write(2, humidity)     # send humidity to V2
        else:
            print("Sensor Error")

        blynk.run()     # handle Blynk communication
        time.sleep(2)   # update delay

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()