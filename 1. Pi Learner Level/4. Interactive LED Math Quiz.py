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
green_led = 21  # Correct answer LED
red_led = 16    # Wrong answer LED

# GPIO setup
gpio.setmode(gpio.BCM)           
gpio.setup(green_led, gpio.OUT) 
gpio.setup(red_led, gpio.OUT)  

# Generate a random multiplication question
def generate_question():
    num1 = random.randint(1, 10)             
    num2 = random.randint(1, 10)             
    return num1, num2, num1 * num2        

try:
    while True:
        num1, num2, correct_answer = generate_question()  
        user_answer = int(input(f"What is {num1} * {num2}?: "))  

        if user_answer == correct_answer:
            gpio.output(green_led, gpio.HIGH)  # Turn ON Green LED
            gpio.output(red_led, gpio.LOW)     # Turn OFF Red LED
            print("Correct! Green LED is ON.")
        else:
            gpio.output(green_led, gpio.LOW)   # Turn OFF Green LED
            gpio.output(red_led, gpio.HIGH)    # Turn ON Red LED
            print(f"Wrong! Red LED is ON. The correct answer is {correct_answer}.")

        time.sleep(2)  # Pause before next question

        # Turn OFF both LEDs before the next question
        gpio.output(green_led, gpio.LOW)
        gpio.output(red_led, gpio.LOW)

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings on exit

