"""
Components Used:
1. Raspberry Pi
2. RGB LED (Common Cathode)
3. Push Button
4. Breadboard
5. Jumper Wires
"""

import RPi.GPIO as gpio
import time
import random

red_pin = 21     # GPIO pin for red LED
green_pin = 20   # GPIO pin for green LED
blue_pin = 16    # GPIO pin for blue LED
button_pin = 12  # GPIO pin for button

gpio.setmode(gpio.BCM)            # Use BCM pin numbering
gpio.setup(red_pin, gpio.OUT)     # Set red pin as output
gpio.setup(green_pin, gpio.OUT)   # Set green pin as output
gpio.setup(blue_pin, gpio.OUT)    # Set blue pin as output
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set button as input

try:
    while True:
        if gpio.input(button_pin) == 0:  # Check button press
            time.sleep(0.1)  # Small delay

            while gpio.input(button_pin) == 0:  # Wait until release
                pass

            red_state = random.randint(0, 1)    # Random red value
            green_state = random.randint(0, 1)  # Random green value
            blue_state = random.randint(0, 1)   # Random blue value

            gpio.output(red_pin, red_state)     # Set red LED
            gpio.output(green_pin, green_state) # Set green LED
            gpio.output(blue_pin, blue_state)   # Set blue LED

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit