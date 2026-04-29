"""
Components Used:
1. Raspberry Pi
2. I2C LCD Display (16x2)
3. Buzzer
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

import time
from RPLCD.i2c import CharLCD
import RPi.GPIO as gpio

buzzer = 21  # GPIO pin for buzzer

gpio.setmode(gpio.BCM)         # Use BCM numbering
gpio.setup(buzzer, gpio.OUT)   # Set buzzer as output

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

    # Buzzer alert
    for _ in range(3):
        gpio.output(buzzer, gpio.HIGH)  # Buzzer ON
        time.sleep(0.5)
        gpio.output(buzzer, gpio.LOW)   # Buzzer OFF
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

finally:
    gpio.cleanup()  # Always cleanup GPIO
    lcd.clear()     # Clear LCD on exit