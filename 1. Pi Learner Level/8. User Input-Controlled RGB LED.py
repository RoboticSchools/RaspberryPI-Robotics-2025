"""
Components Used:
- Raspberry Pi
- RGB LED (Common Cathode)
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
red_pin = 21   
green_pin = 20 
blue_pin = 16

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(red_pin, gpio.OUT)  
gpio.setup(green_pin, gpio.OUT)  
gpio.setup(blue_pin, gpio.OUT) 

try:
    while True:
        user_input = input("Enter color (r, g, b, y, m, c, w): ").lower()

        # Red
        if user_input == "r":  
            gpio.output(red_pin, gpio.HIGH)
            gpio.output(green_pin, gpio.LOW)
            gpio.output(blue_pin, gpio.LOW)
            print("Red LED is ON")

        # Green
        elif user_input == "g":  
            gpio.output(red_pin, gpio.LOW)
            gpio.output(green_pin, gpio.HIGH)
            gpio.output(blue_pin, gpio.LOW)
            print("Green LED is ON")

        # Blue
        elif user_input == "b":  
            gpio.output(red_pin, gpio.LOW)
            gpio.output(green_pin, gpio.LOW)
            gpio.output(blue_pin, gpio.HIGH)
            print("Blue LED is ON")

        # Yellow (Red + Green)
        elif user_input == "y":  
            gpio.output(red_pin, gpio.HIGH)
            gpio.output(green_pin, gpio.HIGH)
            gpio.output(blue_pin, gpio.LOW)
            print("Yellow LED is ON")

        # Magenta (Red + Blue)
        elif user_input == "m":  
            gpio.output(red_pin, gpio.HIGH)
            gpio.output(green_pin, gpio.LOW)
            gpio.output(blue_pin, gpio.HIGH)
            print("Magenta LED is ON")

        # Cyan (Green + Blue)
        elif user_input == "c":  
            gpio.output(red_pin, gpio.LOW)
            gpio.output(green_pin, gpio.HIGH)
            gpio.output(blue_pin, gpio.HIGH)
            print("Cyan LED is ON")

        # White (Red + Green + Blue)
        elif user_input == "w":  
            gpio.output(red_pin, gpio.HIGH)
            gpio.output(green_pin, gpio.HIGH)
            gpio.output(blue_pin, gpio.HIGH)
            print("White LED is ON")

        else:
            print("Invalid input! Enter r, g, b, y, m, c, or w.")

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings on exit
