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
green_led = 21   
yellow_led = 16  
red_led = 12 

# GPIO setup
gpio.setmode(gpio.BCM)  # Use BCM pin numbering
gpio.setup(green_led, gpio.OUT)
gpio.setup(yellow_led, gpio.OUT)
gpio.setup(red_led, gpio.OUT)

# Generate random number between 1 and 10
target_number = random.randint(1, 10)

# Initialize guess counter
guess_count = 0

try:
    while True:
        user_guess = int(input("Guess a number between 1 and 10: "))
        guess_count += 1  # Increment guess count

        if user_guess == target_number:
            gpio.output(green_led, gpio.HIGH)
            gpio.output(yellow_led, gpio.LOW)
            gpio.output(red_led, gpio.LOW)
            print(f"Correct! Green LED is ON. You took {guess_count} guess(es).")
            time.sleep(2)
            break
        elif user_guess < target_number:
            gpio.output(green_led, gpio.LOW)
            gpio.output(yellow_led, gpio.HIGH)
            gpio.output(red_led, gpio.LOW)
            print("Too low! Yellow LED is ON.")
        else:
            gpio.output(green_led, gpio.LOW)
            gpio.output(yellow_led, gpio.LOW)
            gpio.output(red_led, gpio.HIGH)
            print("Too high! Red LED is ON.")

        time.sleep(2)
        gpio.output(green_led, gpio.LOW)
        gpio.output(yellow_led, gpio.LOW)
        gpio.output(red_led, gpio.LOW)

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings on exit
