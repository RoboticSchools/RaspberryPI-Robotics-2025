"""
Components Used:
- Raspberry Pi
- PIR Motion Sensor
- LED
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
pir_pin = 21
led_pin = 20 

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(pir_pin, gpio.IN)  # Set PIR sensor pin as input
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output

try:
    while True:
        if gpio.input(pir_pin) == 1:  # Motion detected
            gpio.output(led_pin, gpio.HIGH)  # Turn LED ON
            print("Motion Detected - LED ON")
        else:  # No motion
            gpio.output(led_pin, gpio.LOW)  # Turn LED OFF
            print("No Motion - LED OFF")

        time.sleep(0.5)  # Small delay for stable readings

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings before exiting
