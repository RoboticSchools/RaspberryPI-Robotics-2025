"""
Components Used:
- Raspberry Pi
- I2C LCD Display (16x2)
- Jumper Wires
"""

import time
from RPLCD.i2c import CharLCD

# Initialize I2C LCD (address 0x27 or 0x3F, check using `i2cdetect -y 1`)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, backlight_enabled=True)

try:
    while True:
        # Get user input
        user_text = input("Enter text (max 15 chars): ")

        # Validate input length
        if len(user_text) > 15:
            print("Error: Text must be 15 characters or less.")
            continue

        # Clear LCD before displaying new text
        lcd.clear()

        # Display user input on LCD
        lcd.cursor_pos = (0, 0)  # First row
        lcd.write_string(user_text)

except KeyboardInterrupt:
    lcd.clear()  # Clear display before exit
