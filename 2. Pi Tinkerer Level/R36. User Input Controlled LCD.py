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

try:
    while True:
        user_text = input("Enter text (max 15 chars): ")  # Get user input
        row = int(input("Enter row (0 or 1): "))  # Get row input

        if len(user_text) > 15:  # Validate length
            print("Error: Max 15 characters allowed")
            continue

        if row not in [0, 1]:  # Validate row
            print("Error: Row must be 0 or 1")
            continue

        lcd.clear()  # Clear display

        lcd.cursor_pos = (row, 0)  # Set selected row
        lcd.write_string(user_text)  # Display text

        time.sleep(0.5)  # Small delay for smooth update

except KeyboardInterrupt:
    lcd.clear()  # Clear LCD on exit