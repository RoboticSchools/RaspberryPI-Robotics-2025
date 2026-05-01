"""
Components Used:
1. Raspberry Pi
2. 4x4 Keypad
3. I2C LCD Display
4. Jumper Wires
"""

import time
import RPi.GPIO as gpio
from RPLCD.i2c import CharLCD

# ---------------- LCD Setup ----------------
lcd_display = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)

# ---------------- Keypad Layout ----------------
keypad_layout = [
    ["1","2","3","A"],
    ["4","5","6","B"],
    ["7","8","9","C"],
    ["*","0","#","D"]
]

# Define GPIO pins for rows and columns
row_pins = [5, 6, 13, 19]
column_pins = [12, 16, 20, 21]

# ---------------- GPIO Setup ----------------
gpio.setmode(gpio.BCM)  # Use BCM numbering

# Set row pins as OUTPUT (default HIGH)
for row_pin in row_pins:
    gpio.setup(row_pin, gpio.OUT)
    gpio.output(row_pin, gpio.HIGH)

# Set column pins as INPUT with pull-down
for column_pin in column_pins:
    gpio.setup(column_pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

# ---------------- Voting Data ----------------
vote_counts = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
}

# ---------------- Function: Read Keypad ----------------
def read_keypad():
    """
    Scan keypad:
    1. Set one row LOW at a time
    2. Check all column pins
    3. If HIGH detected → key pressed
    """
    for row_index, row_pin in enumerate(row_pins):
        gpio.output(row_pin, gpio.LOW)  # Activate row

        for col_index, column_pin in enumerate(column_pins):
            if gpio.input(column_pin) == gpio.HIGH:
                time.sleep(0.2)  # Debounce delay
                gpio.output(row_pin, gpio.HIGH)
                return keypad_layout[row_index][col_index]

        gpio.output(row_pin, gpio.HIGH)  # Deactivate row

    return None  # No key pressed

# ---------------- Main Program ----------------
try:
    lcd_display.clear()
    lcd_display.write_string("A B C D Vote")

    while True:
        pressed_key = read_keypad()  # Read keypad

        if pressed_key:
            lcd_display.clear()

            # ---- Voting ----
            if pressed_key in vote_counts:
                vote_counts[pressed_key] += 1
                lcd_display.write_string("Voted " + pressed_key)

            # ---- Show Results ----
            elif pressed_key == "#":
                lcd_display.write_string(
                    "A:" + str(vote_counts["A"]) + " B:" + str(vote_counts["B"]) + "\n" +
                    "C:" + str(vote_counts["C"]) + " D:" + str(vote_counts["D"])
                )
                time.sleep(3)

            # Return to menu
            time.sleep(2)
            lcd_display.clear()
            lcd_display.write_string("A B C D Vote")

        time.sleep(0.1)  # Small delay

# ---------------- Cleanup ----------------
except KeyboardInterrupt:
    gpio.cleanup()
    lcd_display.clear()
    print("Program stopped")