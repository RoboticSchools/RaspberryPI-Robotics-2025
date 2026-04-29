"""
Components Used:
1. Raspberry Pi
2. I2C LCD Display (16x2)
3. Breadboard
4. Jumper Wires

Install Required Library:
pip install RPLCD smbus2 --break-system-packages

Note:
Check I2C address using:
i2cdetect -y 1

Common addresses:
0x27 or 0x3F
"""

from RPLCD.i2c import CharLCD
import time

# Initialize LCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16,rows=2)

lcd.clear()  # Clear display

lcd.cursor_pos = (0, 0)  # First row
lcd.write_string("Countdown Timer")

try:
    for i in range(10, -1, -1):  # Countdown from 10 to 0
        lcd.cursor_pos = (1, 0)  # Second row
        lcd.write_string(f"Time: {i:<5}")  # Display time (clean formatting)
        time.sleep(1)

    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Time Up!")  # Final message

except KeyboardInterrupt:
    lcd.clear()     # Clear LCD on exit