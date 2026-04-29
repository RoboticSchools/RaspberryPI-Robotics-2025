"""
Components Used:
1. Raspberry Pi
2. 4x4 Matrix Keypad
3. RGB LED
4. Breadboard
5. Jumper Wires
"""

import time
import RPi.GPIO as GPIO
from pad4pi import Keypad

# ---------------- GPIO Setup ----------------
GPIO.setmode(GPIO.BCM)  # use BCM numbering

red_pin = 17    # RED pin
green_pin = 27  # GREEN pin
blue_pin = 22   # BLUE pin

# set RGB pins as output
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# ---------------- Keypad Setup ----------------
keypad_layout = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

row_pins = [5, 6, 13, 19]   # row pins
col_pins = [12, 16, 20, 21] # column pins

factory = Keypad.factory()
keypad = factory.create_keypad(
    keypad=keypad_layout,
    row_pins=row_pins,
    col_pins=col_pins
)

# ---------------- RGB Control Function ----------------
def set_color(r, g, b):
    GPIO.output(red_pin, r)     # control RED
    GPIO.output(green_pin, g)   # control GREEN
    GPIO.output(blue_pin, b)    # control BLUE

# ---------------- Key Press Handler ----------------
def on_key_pressed(key):
    print(f"Key Pressed: {key}")

    # select color based on key
    if key == "1":
        set_color(1, 0, 0)  # Red
    elif key == "2":
        set_color(0, 1, 0)  # Green
    elif key == "3":
        set_color(0, 0, 1)  # Blue
    elif key == "4":
        set_color(1, 1, 0)  # Yellow
    elif key == "5":
        set_color(1, 0, 1)  # Magenta
    elif key == "6":
        set_color(0, 1, 1)  # Cyan
    elif key == "7":
        set_color(1, 1, 1)  # White
    elif key == "0":
        set_color(0, 0, 0)  # OFF

keypad.registerKeyPressHandler(on_key_pressed)

# ---------------- Main Loop ----------------
try:
    print("RGB 8 Color Control Started...")

    while True:
        time.sleep(0.1)  # keep program running

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()  # reset GPIO