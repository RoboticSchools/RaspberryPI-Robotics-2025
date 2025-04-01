"""
Components Used:
- Raspberry Pi
- 4x4 Keypad (Matrix Type)
- Servo Motor (SG90)
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
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

# Define GPIO pins for keypad rows and columns
ROW_PINS = [5, 6, 13, 19]  # Connected to Raspberry Pi GPIO
COL_PINS = [12, 16, 20, 21]  # Connected to Raspberry Pi GPIO

# Initialize keypad using the pad4pi library
factory = Keypad.factory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

# Servo motor setup
SERVO_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz PWM frequency
servo.start(0)

# Password variables
password = "1234"
input_password = ""

# Function to move servo
def unlock_door():
    servo.ChangeDutyCycle(7.5)  # Rotate to 90 degrees (unlock)
    time.sleep(3)
    servo.ChangeDutyCycle(2.5)  # Rotate back to 0 degrees (lock)

# Display initial message on LCD
lcd.clear()
lcd.write_string("Enter Password:")

# Function to handle key press events
def key_pressed(key):
    global input_password
    lcd.clear()

    if key not in ("#", "*"):  # Add key to password input
        input_password += key
        lcd.write_string(input_password)

    elif key == "#":  # Submit password
        lcd.clear()
        if input_password == password:
            lcd.write_string("Access Granted")
            unlock_door()
        else:
            lcd.write_string("Access Denied")

        time.sleep(2)
        input_password = ""  # Reset input
        lcd.clear()
        lcd.write_string("Enter Password:")

    elif key == "*":  # Clear input
        input_password = ""
        lcd.clear()
        lcd.write_string("Enter Password:")

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
