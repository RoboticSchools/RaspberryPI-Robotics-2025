"""
Components Used:
- Raspberry Pi
- Green LED (Correct Answer)  
- Red LED (Wrong Answer)
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time
import random

# Pin configuration
green_led = 21  # GPIO21 for correct answer (Green LED)
red_led = 20    # GPIO20 for wrong answer (Red LED)

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(green_led, gpio.OUT)  # Set Green LED pin as output
gpio.setup(red_led, gpio.OUT)  # Set Red LED pin as output

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 + num2
    return num1, num2, correct_answer

try:
    while True:
        num1, num2, correct_answer = generate_question()
        user_answer = int(input(f"What is {num1} + {num2}?: "))

        if user_answer == correct_answer:
            gpio.output(green_led, gpio.HIGH)  # Turn on Green LED for correct answer
            gpio.output(red_led, gpio.LOW)  # Turn off Red LED
            print("Correct! Green LED is ON.")
        else:
            gpio.output(green_led, gpio.LOW)  # Turn off Green LED
            gpio.output(red_led, gpio.HIGH)  # Turn on Red LED for wrong answer
            print("Wrong! Red LED is ON.")
        
        time.sleep(2)  # Wait before next question
        gpio.output(green_led, gpio.LOW)  # Turn off Green LED
        gpio.output(red_led, gpio.LOW)  # Turn off Red LED

except KeyboardInterrupt:
    pass

gpio.cleanup()  # Reset GPIO settings on exit
