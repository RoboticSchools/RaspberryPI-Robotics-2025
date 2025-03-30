"""
Components Used:
- Raspberry Pi
- I2C LCD Display (16x2)
- Buzzer
- Breadboard
- Jumper Wires
"""

import time
from RPLCD.i2c import CharLCD
import RPi.GPIO as gpio

# Pin configuration
buzzer = 21  # Buzzer connected to GPIO21

# Initialize I2C LCD (address 0x27 or 0x3F, check using `i2cdetect -y 1`)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, backlight_enabled=True)

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(buzzer, gpio.OUT)  # Set buzzer pin as output

# Display title on LCD
lcd.cursor_pos = (0, 0)
lcd.write_string("Countdown Timer")

try:
    for i in range(10, -1, -1):
        lcd.cursor_pos = (1, 0)  # Move to second row
        lcd.write_string(f"Time: {i}      ")  # Display countdown
        time.sleep(1)

    lcd.cursor_pos = (1, 0)
    lcd.write_string("Time Up!      ")  # Display message after countdown

    # Buzzer beeps 3 times
    for _ in range(3):
        gpio.output(buzzer, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(buzzer, gpio.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

# Cleanup GPIO
gpio.cleanup()
