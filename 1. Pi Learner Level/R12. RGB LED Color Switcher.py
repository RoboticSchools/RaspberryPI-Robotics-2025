"""
Components Used:
- Raspberry Pi
- RGB LED (Common Cathode)
- Push Button
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time
import random

# Pin configuration
red_pin = 21    
green_pin = 20
blue_pin = 16
button_pin = 12

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(red_pin, gpio.OUT)
gpio.setup(green_pin, gpio.OUT)
gpio.setup(blue_pin, gpio.OUT)
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set button pin as input with internal pull-up resistor

try:
    while True:
        if gpio.input(button_pin) == 0:  # If button is pressed
            time.sleep(0.1)  # Simple debounce
            
            while gpio.input(button_pin) == 0:  # Wait for button release
                pass
            
            # Generate random states (0 or 1) for each LED color
            red_state = random.randint(0, 1)
            green_state = random.randint(0, 1)
            blue_state = random.randint(0, 1)

            # Set the RGB LED to the new random color
            gpio.output(red_pin, red_state)
            gpio.output(green_pin, green_state)
            gpio.output(blue_pin, blue_state)

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings before exiting
