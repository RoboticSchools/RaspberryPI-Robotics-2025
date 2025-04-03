"""
Components Used:
- Raspberry Pi
- I2C LCD Display (16x2)
- Breadboard
- Jumper Wires
"""

import time
from RPLCD.i2c import CharLCD

# Initialize I2C LCD (address 0x27 or 0x3F, check using `i2cdetect -y 1`)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, backlight_enabled=True)

# Display names on LCD
lcd.cursor_pos = (0, 0)  # Set cursor position to the first row, first column
lcd.write_string("Raspberry Pi")

lcd.cursor_pos = (1, 0)  # Set cursor position to the second row, first column
lcd.write_string("Robotics")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    lcd.clear()  # Clear display before exit
