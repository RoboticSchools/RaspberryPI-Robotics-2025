"""
Components Used:
1. Raspberry Pi
2. I2C LCD Display (16x2)
3. Jumper Wires

Install Required Library:
pip install RPLCD smbus2 --break-system-packages

Note:
If LCD is not displaying, check I2C address using:
i2cdetect -y 1

Common addresses:
0x27 or 0x3F
"""

import time
from RPLCD.i2c import CharLCD

# Initialize LCD (change address if needed)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)

try:
    lcd.clear()  # Clear display

    lcd.cursor_pos = (0, 0)  # First row
    lcd.write_string("Raspberry Pi")

    lcd.cursor_pos = (1, 0)  # Second row
    lcd.write_string("Robotics")

    while True:
        time.sleep(1)  # Keep running

except KeyboardInterrupt:
    lcd.clear()  # Clear display on exit