"""
Components Used:
- Raspberry Pi
- 4x4 Keypad (Matrix Type)
- I2C LCD Display (PCF8574)
- Jumper Wires
"""

import time
import RPi.GPIO as GPIO
from pad4pi import Keypad
from RPLCD.i2c import CharLCD

# Initialize LCD (I2C address 0x27, 16x2 display)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)

# Define the keypad layout (4x4 matrix)
KEYPAD = [
    ["1", "2", "3", "+"],
    ["4", "5", "6", "-"],
    ["7", "8", "9", "*"],
    ["C", "0", "=", "/"]
]

# Define GPIO pins for keypad rows and columns
ROW_PINS = [5, 6, 13, 19]  # Connected to Raspberry Pi GPIO
COL_PINS = [12, 16, 20, 21]  # Connected to Raspberry Pi GPIO

# Initialize keypad using the pad4pi library
factory = Keypad.factory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

# Variable to store the input expression
expression = ""

# Display initial message on LCD
lcd.clear()
lcd.write_string("Enter Numbers:")

# Function to handle key press events
def key_pressed(key):
    global expression

    if key.isdigit() or key in ["+", "-", "*", "/"]:  # Add key to expression
        expression += key
        lcd.write_string(key)

    elif key == "=":  # Evaluate expression
        try:
            result = eval(expression)  # Evaluate using Python's eval()
            lcd.clear()
            lcd.write_string(f"= {result}")
            time.sleep(3)
        except Exception:
            lcd.clear()
            lcd.write_string("Error")

        expression = ""  # Reset input
        lcd.clear()
        lcd.write_string("Enter Numbers:")

    elif key == "C":  # Clear expression
        expression = ""
        lcd.clear()
        lcd.write_string("Enter Numbers:")

# Register keypad event handler
keypad.registerKeyPressHandler(key_pressed)

try:
    while True:
        time.sleep(0.1)  # Prevent excessive CPU usage

except KeyboardInterrupt:
    print("\nExiting...")
    GPIO.cleanup()  # Cleanup GPIO on exit
    lcd.clear()
    lcd.write_string("System Stopped")
    time.sleep(2)
