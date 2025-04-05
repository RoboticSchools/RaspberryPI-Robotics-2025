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

def scroll_text(text):
    """ Scrolls text on the first row of the LCD once and then returns """
    text = text + " " * 16  # Add spaces to create a smooth scrolling effect
    
    for i in range(len(text) - 15):
        lcd.cursor_pos = (0, 0)
        lcd.write_string(text[i:i+16])  # Display scrolling portion
        time.sleep(0.3)

try:
    while True:
        user_text = input("Enter text to display: ")  # Get user input
        lcd.clear()  # Clear LCD before displaying new text
        scroll_text(user_text)

except KeyboardInterrupt:
    lcd.clear()  # Clear display before exit
