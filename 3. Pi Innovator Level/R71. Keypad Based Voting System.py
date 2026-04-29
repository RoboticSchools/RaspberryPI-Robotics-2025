"""
Components Used:
1. Raspberry Pi
2. 4x4 Keypad (Matrix Type)
3. I2C LCD Display (PCF8574)
4. Jumper Wires
"""

import time
import sys
import RPi.GPIO as GPIO
from pad4pi import Keypad
from RPLCD.i2c import CharLCD

# ---------------- LCD Setup ----------------
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)

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

# ---------------- Voting Data ----------------
vote_counts = {"A": 0, "B": 0, "C": 0, "D": 0}  # store votes

# ---------------- Display Functions ----------------
def show_intro():
    lcd.clear()
    lcd.write_string("Get Ready\nTo Vote!")
    time.sleep(3)
    lcd.clear()

def show_options():
    lcd.clear()
    lcd.write_string("Vote A  Vote B\nVote C  Vote D")

# ---------------- Key Press Handler ----------------
def on_key_pressed(key):
    lcd.clear()

    if key in vote_counts:
        vote_counts[key] += 1          # increase vote count
        lcd.write_string(f"Voted {key}")

    elif key == "#":                  # show results
        lcd.write_string(f"A:{vote_counts['A']} B:{vote_counts['B']}\n")
        lcd.write_string(f"C:{vote_counts['C']} D:{vote_counts['D']}")
        time.sleep(3)

        # find highest votes
        max_votes = max(vote_counts.values())

        # get winner(s)
        winners = [k for k, v in vote_counts.items() if v == max_votes]

        lcd.clear()
        lcd.write_string("Winner(s):\n" + " ".join(winners))
        time.sleep(5)

        GPIO.cleanup()                # cleanup GPIO
        lcd.clear()
        lcd.write_string("Voting Done")
        time.sleep(2)
        sys.exit()                    # exit program

    time.sleep(2)
    show_options()                    # show menu again

keypad.registerKeyPressHandler(on_key_pressed)

# ---------------- Main Loop ----------------
try:
    show_intro()      # display welcome
    show_options()    # display options

    while True:
        time.sleep(0.1)  # keep program running

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()      # reset GPIO
    lcd.clear()
    lcd.write_string("System Stopped")
    time.sleep(2)