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
red_pin = 21    # GPIO21 connected to the Red pin of RGB LED
green_pin = 20  # GPIO20 connected to the Green pin of RGB LED
blue_pin = 16   # GPIO16 connected to the Blue pin of RGB LED

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(red_pin, gpio.OUT)  # Set Red pin as output
gpio.setup(green_pin, gpio.OUT)  # Set Green pin as output
gpio.setup(blue_pin, gpio.OUT)  # Set Blue pin as output

try:
    while True:
        user_input = input("Enter color (red, green, blue, yellow, magenta, cyan, white): ").strip().lower()

        if user_input == "red":
            gpio.output(red_pin, gpio.HIGH)
            gpio.output(green_pin, gpio.LOW)
            gpio.output(blue_pin, gpio.LOW)
            print("Red LED is ON")

        elif user_input == "green":
            gpio.output(red_pin, gpio.LOW)
            gpio.output(green_pin, gpio.HIGH)
            gpio.output(blue_pin, gpio.LOW)
            print("Green LED is ON")

        elif user_input == "blue":
            gpio.output(red_pin, gpio.LOW)
            gpio.output(green_pin, gpio.LOW)
            gpio.output(blue_pin, gpio.HIGH)
            print("Blue LED is ON")

        elif user_input == "yellow":  # Red + Green
            gpio.output(red_pin, gpio.HIGH)
            gpio.output(green_pin, gpio.HIGH)
            gpio.output(blue_pin, gpio.LOW)
            print("Yellow LED is ON")

        elif user_input == "magenta":  # Red + Blue
            gpio.output(red_pin, gpio.HIGH)
            gpio.output(green_pin, gpio.LOW)
            gpio.output(blue_pin, gpio.HIGH)
            print("Magenta LED is ON")

        elif user_input == "cyan":  # Green + Blue
            gpio.output(red_pin, gpio.LOW)
            gpio.output(green_pin, gpio.HIGH)
            gpio.output(blue_pin, gpio.HIGH)
            print("Cyan LED is ON")

        elif user_input == "white":  # Red + Green + Blue
            gpio.output(red_pin, gpio.HIGH)
            gpio.output(green_pin, gpio.HIGH)
            gpio.output(blue_pin, gpio.HIGH)
            print("White LED is ON")

        else:
            print("Invalid color! Please enter red, green, blue, yellow, magenta, cyan, or white.")

except KeyboardInterrupt:
    pass

gpio.cleanup()  # Reset GPIO settings on exit
