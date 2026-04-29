"""
Components Used:
1. Raspberry Pi
2. LED
3. Breadboard
4. Jumper Wires
5. Blynk WebApp

Install Required Library:
pip install blynklib --break-system-packages
"""

import RPi.GPIO as gpio
from BlynkLib import Blynk
import time

BLYNK_AUTH = "YOUR_BLYNK_AUTH_TOKEN"  # Enter your Blynk auth token

led_pin = 21  # GPIO pin for LED

gpio.setmode(gpio.BCM)        # Use BCM pin numbering
gpio.setup(led_pin, gpio.OUT) # Set LED as output

blynk = Blynk(BLYNK_AUTH)  # Initialize Blynk

@blynk.on("V0")
def control_led(value):
    if int(value[0]) == 1:
        gpio.output(led_pin, gpio.HIGH)  # Turn LED ON
        print("LED ON - Blynk Button Pressed")
    else:
        gpio.output(led_pin, gpio.LOW)   # Turn LED OFF
        print("LED OFF - Blynk Button Released")

@blynk.on("connected")
def blynk_connected():
    print("Blynk Connected")  # Connection status

try:
    while True:
        blynk.run()  # Run Blynk
        time.sleep(0.1)  # Small delay

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit