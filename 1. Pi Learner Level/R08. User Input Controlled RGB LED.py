"""
Components Used:
1. Raspberry Pi
2. RGB LED (Common Cathode)
3. Breadboard
4. Jumper Wires
"""

import RPi.GPIO as gpio
import time

red_pin = 21    # GPIO pin for red LED
green_pin = 20  # GPIO pin for green LED
blue_pin = 16   # GPIO pin for blue LED

gpio.setmode(gpio.BCM)           # Use BCM pin numbering
gpio.setup(red_pin, gpio.OUT)    # Set red pin as output
gpio.setup(green_pin, gpio.OUT)  # Set green pin as output
gpio.setup(blue_pin, gpio.OUT)   # Set blue pin as output

try:
    while True:
        user_input = input("Enter color (r, g, b, y, m, c, w): ").lower()  # Get input

        if user_input == "r":
            gpio.output(red_pin, gpio.HIGH)    # Red ON
            gpio.output(green_pin, gpio.LOW)
            gpio.output(blue_pin, gpio.LOW)
            print("Red LED is ON")

        elif user_input == "g":
            gpio.output(red_pin, gpio.LOW)
            gpio.output(green_pin, gpio.HIGH)  # Green ON
            gpio.output(blue_pin, gpio.LOW)
            print("Green LED is ON")

        elif user_input == "b":
            gpio.output(red_pin, gpio.LOW)
            gpio.output(green_pin, gpio.LOW)
            gpio.output(blue_pin, gpio.HIGH)   # Blue ON
            print("Blue LED is ON")

        elif user_input == "y":
            gpio.output(red_pin, gpio.HIGH)    # Yellow
            gpio.output(green_pin, gpio.HIGH)
            gpio.output(blue_pin, gpio.LOW)
            print("Yellow LED is ON")

        elif user_input == "m":
            gpio.output(red_pin, gpio.HIGH)    # Magenta
            gpio.output(green_pin, gpio.LOW)
            gpio.output(blue_pin, gpio.HIGH)
            print("Magenta LED is ON")

        elif user_input == "c":
            gpio.output(red_pin, gpio.LOW)
            gpio.output(green_pin, gpio.HIGH)  # Cyan
            gpio.output(blue_pin, gpio.HIGH)
            print("Cyan LED is ON")

        elif user_input == "w":
            gpio.output(red_pin, gpio.HIGH)    # White
            gpio.output(green_pin, gpio.HIGH)
            gpio.output(blue_pin, gpio.HIGH)
            print("White LED is ON")

        else:
            print("Invalid input")

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit