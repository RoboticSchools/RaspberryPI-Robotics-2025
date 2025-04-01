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

# Voting counters for each candidate
vote_counts = {"A": 0, "B": 0, "C": 0, "D": 0}

# Display initial message on LCD
lcd.clear()
lcd.write_string("Get Ready\nTo Vote!")
time.sleep(2)
lcd.clear()

# Function to display voting options
def intro_vote():
    lcd.clear()
    lcd.write_string("Vote A    Vote B\nVote C    Vote D")

intro_vote()

# Function to handle key press events
def key_pressed(key):
    lcd.clear()
    
    if key in vote_counts:
        # Increment the vote count for the pressed key
        vote_counts[key] += 1
        lcd.write_string(f"Voted {key}")

    elif key == "#":  # Display results when "#" is pressed
        lcd.write_string(f"A:{vote_counts['A']} B:{vote_counts['B']}\n")
        lcd.write_string(f"C:{vote_counts['C']} D:{vote_counts['D']}")
        time.sleep(3)

        # Determine the highest vote count
        max_vote = max(vote_counts.values())

        # Find the candidates who received the maximum votes
        winners = [candidate for candidate, votes in vote_counts.items() if votes == max_vote]

        lcd.clear()
        lcd.write_string("Winner(s):\n" + " ".join(winners))
        time.sleep(5)
        return  # Exit function to prevent infinite loop

    time.sleep(3)
    intro_vote()

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
