"""
Components Used:
- Raspberry Pi
- LED
- Push Button
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
led_pin = 21
button_pin = 16

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set button pin as input with internal pull-up resistor

try:
    while True:
        if gpio.input(button_pin) == 0:  # Check if button is pressed (0 due to pull-up)
            gpio.output(led_pin, gpio.HIGH)  # Turn LED on
            print("Button Pressed - LED ON")
        else:
            gpio.output(led_pin, gpio.LOW)  # Turn LED off
            print("Button Released - LED OFF")

        time.sleep(0.1)  # Small delay to avoid bouncing issues

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings on exit
