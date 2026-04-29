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

# setup led pin
led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

# define keypad layout
keypad_layout = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

# define gpio pins for keypad rows and columns
row_pins = [5, 6, 13, 19]
col_pins = [12, 16, 20, 21]

# initialize keypad
factory = Keypad.factory()
keypad = factory.create_keypad(keypad=keypad_layout, row_pins=row_pins, col_pins=col_pins)

# handle key press
def key_pressed(key):
    print(f"Key Pressed: {key}")
    if key == "1":
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED ON")
    elif key == "0":
        GPIO.output(led_pin, GPIO.LOW)
        print("LED OFF")

keypad.registerKeyPressHandler(key_pressed)

# main loop
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
