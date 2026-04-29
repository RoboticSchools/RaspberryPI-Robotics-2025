"""
Components Used:
1. Raspberry Pi
2. I2C LCD Display (16x2)
3. 2 Push Buttons
4. Breadboard
5. Jumper Wires

Install Required Library:
pip install RPLCD smbus2 --break-system-packages

Note:
Check I2C address using:
i2cdetect -y 1

Common addresses:
0x27 or 0x3F
"""

import RPi.GPIO as gpio
from RPLCD.i2c import CharLCD
import time
import random

button_a = 20  # Button A
button_b = 16  # Button B

gpio.setmode(gpio.BCM)  # Use BCM numbering
gpio.setup(button_a, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(button_b, gpio.IN, pull_up_down=gpio.PUD_UP)

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 * num2
    wrong_answer = correct_answer + random.randint(2, 5)

    options = [correct_answer, wrong_answer]
    random.shuffle(options)

    return num1, num2, options, correct_answer

def display_question(num1, num2, options):
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string(f"{num1} x {num2} = ?")

    lcd.cursor_pos = (1, 0)
    lcd.write_string(f"A:{options[0]} B:{options[1]}")

try:
    while True:
        num1, num2, options, correct_answer = generate_question()
        display_question(num1, num2, options)

        while True:
            if gpio.input(button_a) == 0:
                selected_answer = options[0]
                time.sleep(0.2)
                while gpio.input(button_a) == 0:
                    pass
                break

            if gpio.input(button_b) == 0:
                selected_answer = options[1]
                time.sleep(0.2)
                while gpio.input(button_b) == 0:
                    pass
                break

        lcd.clear()
        lcd.cursor_pos = (0, 0)

        if selected_answer == correct_answer:
            lcd.write_string("Correct!")
        else:
            lcd.write_string("Wrong!")

        time.sleep(2)

except KeyboardInterrupt:
    lcd.clear()
    gpio.cleanup()