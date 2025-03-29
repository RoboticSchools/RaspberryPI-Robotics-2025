"""
Components Used:
- Raspberry Pi
- Green LED (Correct Guess)
- Yellow LED (Low Guess)
- Red LED (High Guess)
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time
import random

# Pin configuration
green_led = 21  # GPIO21 for correct guess (Green LED)
yellow_led = 20  # GPIO20 for low guess (Yellow LED)
red_led = 16  # GPIO16 for high guess (Red LED)

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(green_led, gpio.OUT)  # Set Green LED as output
gpio.setup(yellow_led, gpio.OUT)  # Set Yellow LED as output
gpio.setup(red_led, gpio.OUT)  # Set Red LED as output

# Generate random number between 1 and 10
target_number = random.randint(1, 10)

try:
    while True:
        user_guess = int(input("Guess a number between 1 and 10: "))

        if user_guess == target_number:
            gpio.output(green_led, gpio.HIGH)  # Correct guess
            gpio.output(yellow_led, gpio.LOW)
            gpio.output(red_led, gpio.LOW)
            print("Correct! Green LED is ON.")
            time.sleep(2)
            target_number = random.randint(1, 10)  # Generate new number after correct guess
        elif user_guess < target_number:
            gpio.output(green_led, gpio.LOW)
            gpio.output(yellow_led, gpio.HIGH)  # Low guess
            gpio.output(red_led, gpio.LOW)
            print("Too low! Yellow LED is ON.")
        else:
            gpio.output(green_led, gpio.LOW)
            gpio.output(yellow_led, gpio.LOW)
            gpio.output(red_led, gpio.HIGH)  # High guess
            print("Too high! Red LED is ON.")

        time.sleep(2)  # Wait before next guess
        gpio.output(green_led, gpio.LOW)  # Turn off all LEDs
        gpio.output(yellow_led, gpio.LOW)
        gpio.output(red_led, gpio.LOW)

except KeyboardInterrupt:
    pass

gpio.cleanup()  # Reset GPIO settings on exit
