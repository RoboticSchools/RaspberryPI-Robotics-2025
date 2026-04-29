"""
Components Used:
1. Raspberry Pi
2. LDR (Light Sensor)
3. LED
4. Breadboard
5. Jumper Wires
"""

import RPi.GPIO as gpio
import time

ldr_pin = 21  # GPIO pin for LDR
led_pin = 20  # GPIO pin for LED

gpio.setmode(gpio.BCM)        # Use BCM pin numbering
gpio.setup(ldr_pin, gpio.IN)  # Set LDR as input
gpio.setup(led_pin, gpio.OUT) # Set LED as output

try:
    while True:
        if gpio.input(ldr_pin) == 1:  # Check dark condition
            gpio.output(led_pin, gpio.HIGH)  # Turn LED ON
            print("Dark detected - LED ON")
        else:
            gpio.output(led_pin, gpio.LOW)   # Turn LED OFF
            print("Light detected - LED OFF")

        time.sleep(1)  # Small delay

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit