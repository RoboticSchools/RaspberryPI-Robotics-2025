"""
Components Used:
- Raspberry Pi
- 4x4 Matrix Keypad
- LED
- Jumper Wires
- Breadboard
"""

import RPi.GPIO as GPIO
from pad4pi import Keypad
import time

# GPIO Pin Configuration
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Define the Keypad Layout
KEYPAD = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

# Define GPIO Pins for Keypad Rows and Columns
ROW_PINS = [5, 6, 13, 19]
COL_PINS = [12, 16, 20, 21]

# Initialize Keypad
factory = Keypad.factory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

# Function to Handle Key Presses
def key_pressed(key):
    print(f"Key Pressed: {key}")
    
    if key == "1":
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED ON
        print("LED ON")
    elif key == "0":
        GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED OFF
        print("LED OFF")

# Register the Key Press Event
keypad.registerKeyPressHandler(key_pressed)

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
