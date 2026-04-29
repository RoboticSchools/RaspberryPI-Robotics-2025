"""
Components Used:
1. Raspberry Pi
2. I2C LCD Display (16x2)
3. Jumper Wires

Install Required Library:
pip install RPLCD smbus2 --break-system-packages

Note:
Check I2C address using:
i2cdetect -y 1

Common addresses:
0x27 or 0x3F
"""

import time
from RPLCD.i2c import CharLCD

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)  # LCD init

def scroll_text(text, row, direction):
    text = text + " " * 16  # add spaces for smooth scrolling

    if direction == "left":
        for i in range(len(text) - 15):
            lcd.cursor_pos = (row, 0)            # set row position
            lcd.write_string(text[i:i+16])       # display 16 chars
            time.sleep(0.3)                      # scroll speed

    elif direction == "right":
        for i in range(len(text) - 15):
            lcd.cursor_pos = (row, 0)
            lcd.write_string(text[::-1][i:i+16][::-1])  # reverse scroll
            time.sleep(0.3)

try:
    while True:
        user_text = input("Enter text: ")              # get text
        row = int(input("Enter row (0 or 1): "))       # select row
        direction = input("Direction (left/right): ").lower()  # scroll direction

        lcd.clear()                # clear display
        scroll_text(user_text, row, direction)  # call function

except KeyboardInterrupt:
    lcd.clear()  # clear on exit