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
    ["1", "2", "3", "+"],
    ["4", "5", "6", "-"],
    ["7", "8", "9", "*"],
    ["C", "0", "=", "/"]
]

row_pins = [5, 6, 13, 19]
column_pins = [12, 16, 20, 21]

# ---------------- GPIO Setup ----------------
gpio.setmode(gpio.BCM)

# Set row pins as OUTPUT (default HIGH)
for row_pin in row_pins:
    gpio.setup(row_pin, gpio.OUT)
    gpio.output(row_pin, gpio.HIGH)

# Set column pins as INPUT with pull-down
for column_pin in column_pins:
    gpio.setup(column_pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

# ---------------- Calculator Variable ----------------
expression = ""

# ---------------- Display Initial ----------------
lcd_display.clear()
lcd_display.write_string("Enter Numbers:")

# ---------------- Read Keypad ----------------
def read_keypad():
    for row_index, row_pin in enumerate(row_pins):
        gpio.output(row_pin, gpio.LOW)

        for col_index, column_pin in enumerate(column_pins):
            if gpio.input(column_pin) == gpio.HIGH:
                time.sleep(0.2)  # debounce
                gpio.output(row_pin, gpio.HIGH)
                return keypad_layout[row_index][col_index]

        gpio.output(row_pin, gpio.HIGH)

    return None

# ---------------- Main Loop ----------------
try:
    while True:
        pressed_key = read_keypad()

        if pressed_key:
            # ---- Add numbers/operators ----
            if pressed_key.isdigit() or pressed_key in ["+", "-", "*", "/"]:
                expression += pressed_key
                lcd_display.write_string(pressed_key)

            # ---- Evaluate ----
            elif pressed_key == "=":
                try:
                    result = eval(expression)
                    lcd_display.clear()
                    lcd_display.write_string("= " + str(result))
                    time.sleep(3)
                except:
                    lcd_display.clear()
                    lcd_display.write_string("Error")
                    time.sleep(2)

                # Reset
                expression = ""
                lcd_display.clear()
                lcd_display.write_string("Enter Numbers:")

            # ---- Clear ----
            elif pressed_key == "C":
                expression = ""
                lcd_display.clear()
                lcd_display.write_string("Enter Numbers:")

        time.sleep(0.1)

# ---------------- Cleanup ----------------
except KeyboardInterrupt:
    gpio.cleanup()
    lcd_display.clear()
    lcd_display.write_string("Stopped")
    print("Exiting...")