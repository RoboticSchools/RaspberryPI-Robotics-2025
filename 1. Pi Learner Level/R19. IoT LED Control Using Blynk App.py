"""
Components Used:
- Raspberry Pi
- LED
- Blynk Web App
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
from BlynkLib import Blynk
import time

# Blynk authentication token (replace with your actual token)
BLYNK_AUTH = "35MM8LiiGN_EPE96RJsB-wK3E5tlwbxK"

# Pin configuration
led_pin = 21

# GPIO setup
gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)

# Initialize Blynk
blynk = Blynk(BLYNK_AUTH)

# Function to handle virtual pin V0 (LED control)
@blynk.on("V0")
def control_led(value):
    if int(value[0]) == 1:
        gpio.output(led_pin, gpio.HIGH)
        print("LED ON - Blynk Button Pressed")
    else:
        gpio.output(led_pin, gpio.LOW)
        print("LED OFF - Blynk Button Released")

# Function to handle connection
@blynk.on("connected")
def blynk_connected():
    print("Blynk Connected")

try:
    while True:
        blynk.run()
        time.sleep(0.1)

except KeyboardInterrupt:
    gpio.cleanup()
