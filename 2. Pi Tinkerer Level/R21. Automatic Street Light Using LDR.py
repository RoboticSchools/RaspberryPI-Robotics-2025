"""
Components Used:
- Raspberry Pi
- LDR (Light Dependent Resistor)
- LED
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
ldr_pin = 21
led_pin = 20

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(ldr_pin, gpio.IN) 
gpio.setup(led_pin, gpio.OUT) 

try:
    while True:
        if gpio.input(ldr_pin) == 1:  # Dark condition (LDR output 1)
            gpio.output(led_pin, gpio.HIGH)
            print("Dark detected - LED ON")
        else:  # Light condition (LDR output 0)
            gpio.output(led_pin, gpio.LOW)
            print("Light detected - LED OFF")

        time.sleep(1)  # Small delay for stable readings

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings before exiting
