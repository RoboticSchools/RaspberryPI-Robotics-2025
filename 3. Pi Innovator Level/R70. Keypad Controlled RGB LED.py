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

# ---------------- GPIO Setup ----------------
GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbering (GPIO17, GPIO27, etc.)

# RGB LED pins (connect to resistor → LED → GND)
red_pin = 17    # RED LED pin
green_pin = 27  # GREEN LED pin
blue_pin = 22   # BLUE LED pin

# Set RGB pins as OUTPUT so we can control ON/OFF
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# ---------------- Keypad Setup ----------------
# Define keypad button layout (same as physical keypad)
keypad_layout = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

# GPIO pins connected to keypad rows and columns
row_pins = [5, 6, 13, 19]   # Row pins (outputs)
col_pins = [12, 16, 20, 21] # Column pins (inputs)

# Set all row pins as OUTPUT and default HIGH (inactive)
for row in row_pins:
    GPIO.setup(row, GPIO.OUT)
    GPIO.output(row, GPIO.HIGH)

# Set all column pins as INPUT with pull-down resistors
# This ensures stable LOW when no key is pressed
for col in col_pins:
    GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# ---------------- RGB Control Function ----------------
def set_color(r, g, b):
    """
    Control RGB LED color
    r, g, b values:
    1 = ON, 0 = OFF
    """
    GPIO.output(red_pin, r)     # Turn RED ON/OFF
    GPIO.output(green_pin, g)   # Turn GREEN ON/OFF
    GPIO.output(blue_pin, b)    # Turn BLUE ON/OFF

# ---------------- Key Detection Function ----------------
def read_key():
    """
    Scan keypad to detect which key is pressed
    Method:
    1. Activate one row at a time (set LOW)
    2. Check all columns
    3. If column reads HIGH → key is pressed
    """

    for i, row in enumerate(row_pins):
        GPIO.output(row, GPIO.LOW)  # Activate current row

        # Check each column for HIGH signal
        for j, col in enumerate(col_pins):
            if GPIO.input(col) == GPIO.HIGH:
                time.sleep(0.2)  # Debounce delay (avoid multiple detection)

                GPIO.output(row, GPIO.HIGH)  # Deactivate row

                # Return the pressed key from layout
                return keypad_layout[i][j]

        GPIO.output(row, GPIO.HIGH)  # Deactivate row after scanning

    return None  # No key pressed

# ---------------- Main Loop ----------------
try:
    print("RGB 8 Color Control Started...")

    while True:
        key = read_key()  # Check for key press

        if key:
            print(f"Key Pressed: {key}")

            # Map keys to colors
            if key == "1":
                set_color(1, 0, 0)  # Red
            elif key == "2":
                set_color(0, 1, 0)  # Green
            elif key == "3":
                set_color(0, 0, 1)  # Blue
            elif key == "4":
                set_color(1, 1, 0)  # Yellow (Red + Green)
            elif key == "5":
                set_color(1, 0, 1)  # Magenta (Red + Blue)
            elif key == "6":
                set_color(0, 1, 1)  # Cyan (Green + Blue)
            elif key == "7":
                set_color(1, 1, 1)  # White (All ON)
            elif key == "0":
                set_color(0, 0, 0)  # OFF (All OFF)

        time.sleep(0.1)  # Small delay to reduce CPU usage

# ---------------- Cleanup ----------------
except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()  # Reset all GPIO pins safely