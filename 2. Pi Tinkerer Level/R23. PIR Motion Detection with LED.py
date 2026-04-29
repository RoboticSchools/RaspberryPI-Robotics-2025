"""
Components Used:
1. Raspberry Pi
2. PIR Motion Sensor
3. LED
4. Breadboard
5. Jumper Wires
"""

import RPi.GPIO as gpio
import time

pir_pin = 21  # GPIO pin for PIR sensor
led_pin = 20  # GPIO pin for LED

gpio.setmode(gpio.BCM)         # Use BCM pin numbering
gpio.setup(pir_pin, gpio.IN)   # Set PIR as input
gpio.setup(led_pin, gpio.OUT)  # Set LED as output

try:
    while True:
        if gpio.input(pir_pin) == 1:  # Check motion
            gpio.output(led_pin, gpio.HIGH)  # Turn LED ON
            print("Motion Detected - LED ON")
        else:
            gpio.output(led_pin, gpio.LOW)   # Turn LED OFF
            print("No Motion - LED OFF")

        time.sleep(0.5)  # Small delay

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit