"""
Components Used:
- Raspberry Pi
- I2C LCD Display (16x2)
- Two Push Buttons
- Breadboard
- Jumper Wires
"""

import time
import random
import RPi.GPIO as gpio
from RPLCD.i2c import CharLCD

button_a = 20
button_b = 16

lcd = CharLCD(i2c_expander='PCF8574',
              address=0x27,
              port=1,
              cols=16,
              rows=2,
              backlight_enabled=True)

gpio.setmode(gpio.BCM)
gpio.setup(button_a, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(button_b, gpio.IN, pull_up_down=gpio.PUD_UP)

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 * num2
    wrong_answer = correct_answer + random.randint(5, 10)

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
                time.sleep(0.3)
                break

            if gpio.input(button_b) == 0:
                selected_answer = options[1]
                time.sleep(0.3)
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
