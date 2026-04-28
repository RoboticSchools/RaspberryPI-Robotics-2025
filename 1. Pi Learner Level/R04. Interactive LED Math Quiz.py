import RPi.GPIO as gpio
import time
import random

green_led = 21  # GPIO pin for correct answer LED
red_led = 16    # GPIO pin for wrong answer LED

gpio.setmode(gpio.BCM)            # Use BCM pin numbering
gpio.setup(green_led, gpio.OUT)   # Set green LED as output
gpio.setup(red_led, gpio.OUT)     # Set red LED as output

def generate_question():
    num1 = random.randint(1, 10)  # Random number 1
    num2 = random.randint(1, 10)  # Random number 2
    return num1, num2, num1 * num2  # Return question and answer

try:
    while True:
        num1, num2, correct_answer = generate_question()  # Get question
        user_answer = int(input(f"What is {num1} * {num2}?: "))  # Get user input

        if user_answer == correct_answer:
            gpio.output(green_led, gpio.HIGH)  # Turn green LED ON
            gpio.output(red_led, gpio.LOW)     # Turn red LED OFF
            print("Correct! Green LED is ON.")
        else:
            gpio.output(green_led, gpio.LOW)   # Turn green LED OFF
            gpio.output(red_led, gpio.HIGH)    # Turn red LED ON
            print(f"Wrong! Red LED is ON. Answer is {correct_answer}.")

        time.sleep(2)  # Wait before next question

        gpio.output(green_led, gpio.LOW)  # Turn green LED OFF
        gpio.output(red_led, gpio.LOW)    # Turn red LED OFF

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit