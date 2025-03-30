"""
Components Used:
- Raspberry Pi
- LDR (Light Dependent Resistor)
- LED
- Resistors
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
ldr_pin = 21  # GPIO21 connected to LDR (Digital Output)
led_pin = 20  # GPIO20 connected to LED

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(ldr_pin, gpio.IN)  # Set LDR pin as input
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output

try:
    while True:
        if gpio.input(ldr_pin) == gpio.LOW:  # Dark condition (LDR output LOW)
            gpio.output(led_pin, gpio.HIGH)  # Turn LED ON
            print("Dark detected - LED ON")
        else:  # Light condition (LDR output HIGH)
            gpio.output(led_pin, gpio.LOW)  # Turn LED OFF
            print("Light detected - LED OFF")

        time.sleep(1)  # Small delay for stable readings

except KeyboardInterrupt:
    pass

gpio.cleanup()  # Reset GPIO settings before exiting
