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

# Initialize LCD (change address if needed)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)

def scroll_text(text):
    text = text + " " * 16  # Add padding for smooth scroll

    for i in range(len(text) - 15):
        lcd.cursor_pos = (0, 0)          # First row
        lcd.write_string(text[i:i+16])   # Show 16 chars
        time.sleep(0.3)                  # Scroll speed

try:
    while True:
        user_text = input("Enter text to display: ")  # Get input

        lcd.clear()          # Clear display
        scroll_text(user_text)  # Scroll text

except KeyboardInterrupt:
    lcd.clear()  # Clear display on exit