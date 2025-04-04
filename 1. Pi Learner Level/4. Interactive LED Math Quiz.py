"""
Components Used:
- Raspberry Pi
- Green LED (Correct Answer)  
- Red LED (Wrong Answer)
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio  # Import Raspberry Pi GPIO library
import time              # Import time module for delays
import random            # Import random module for question generation

# Pin configuration
green_led = 21  # GPIO21 for correct answer (Green LED)
red_led = 20    # GPIO20 for wrong answer (Red LED)

# GPIO setup
gpio.setmode(gpio.BCM)           # Use BCM pin numbering
gpio.setup(green_led, gpio.OUT)  # Set Green LED pin as output
gpio.setup(red_led, gpio.OUT)    # Set Red LED pin as output

# Function to generate a random addition question
def generate_question():
    num1 = random.randint(1, 10)             # Generate first number
    num2 = random.randint(1, 10)             # Generate second number
    correct_answer = num1 + num2             # Calculate correct answer
    return num1, num2, correct_answer        # Return values

try:
    while True:
        num1, num2, correct_answer = generate_question()  # Generate new question
        user_answer = int(input(f"What is {num1} + {num2}?: "))  # Get user input

        if user_answer == correct_answer:
            gpio.output(green_led, gpio.HIGH)  # Turn ON Green LED for correct answer
            gpio.output(red_led, gpio.LOW)     # Ensure Red LED is OFF
            print("Correct! Green LED is ON.")
        else:
            gpio.output(green_led, gpio.LOW)   # Ensure Green LED is OFF
            gpio.output(red_led, gpio.HIGH)    # Turn ON Red LED for wrong answer
            print(f"Wrong! Red LED is ON. The correct answer is {correct_answer}.")

        time.sleep(2)  # Wait for 2 seconds before the next question

        # Turn OFF both LEDs before the next question
        gpio.output(green_led, gpio.LOW)
        gpio.output(red_led, gpio.LOW)

except KeyboardInterrupt:
    pass  # Exit the loop if Ctrl+C is pressed

gpio.cleanup()  # Reset all GPIO settings before exiting
