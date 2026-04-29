"""
Components Used:
1. Raspberry Pi
2. LED
3. Breadboard
4. Jumper Wires
"""

import RPi.GPIO as gpio
import time

led_pin = 21  # GPIO pin connected to LED

gpio.setmode(gpio.BCM)       # Use BCM pin numbering
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output

try:
    while True:
        gpio.output(led_pin, gpio.HIGH)  # Turn LED ON
        print("LED is ON")
        time.sleep(1)  # Wait 1 second

        gpio.output(led_pin, gpio.LOW)   # Turn LED OFF
        print("LED is OFF")
        time.sleep(1)  # Wait 1 second

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit