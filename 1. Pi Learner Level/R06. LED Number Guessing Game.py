"""
Components Used:
1. Raspberry Pi
2. Green LED
3. Yellow LED
4. Red LED
5. Breadboard
6. Jumper Wires
"""

import RPi.GPIO as gpio
import time
import random

green_led = 21   # GPIO pin for correct guess LED
yellow_led = 16  # GPIO pin for low guess LED
red_led = 12     # GPIO pin for high guess LED

gpio.setmode(gpio.BCM)           # Use BCM pin numbering
gpio.setup(green_led, gpio.OUT)  # Set green LED as output
gpio.setup(yellow_led, gpio.OUT) # Set yellow LED as output
gpio.setup(red_led, gpio.OUT)    # Set red LED as output

target_number = random.randint(1, 10)  # Generate random number
guess_count = 0  # Count guesses

try:
    while True:
        user_guess = int(input("Guess a number between 1 and 10: "))  # Get input
        guess_count += 1  # Increase count

        if user_guess == target_number:
            gpio.output(green_led, gpio.HIGH)  # Turn green LED ON
            gpio.output(yellow_led, gpio.LOW)
            gpio.output(red_led, gpio.LOW)
            print(f"Correct! You took {guess_count} guess(es).")
            time.sleep(2)
            break  # Exit loop

        elif user_guess < target_number:
            gpio.output(green_led, gpio.LOW)
            gpio.output(yellow_led, gpio.HIGH)  # Turn yellow LED ON
            gpio.output(red_led, gpio.LOW)
            print("Too low!")

        else:
            gpio.output(green_led, gpio.LOW)
            gpio.output(yellow_led, gpio.LOW)
            gpio.output(red_led, gpio.HIGH)  # Turn red LED ON
            print("Too high!")

        time.sleep(2)  # Wait before next guess

        gpio.output(green_led, gpio.LOW)  # Turn all LEDs OFF
        gpio.output(yellow_led, gpio.LOW)
        gpio.output(red_led, gpio.LOW)

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit