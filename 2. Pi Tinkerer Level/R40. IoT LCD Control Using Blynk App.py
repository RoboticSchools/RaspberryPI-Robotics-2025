"""
Components Used:
- Raspberry Pi
- I2C LCD Display (16x2)
- Blynk App
- Jumper Wires
"""

import time
import RPi.GPIO as gpio
from BlynkLib import Blynk
from RPLCD.i2c import CharLCD

# Blynk authentication token (replace with your actual token)
BLYNK_AUTH = "35MM8LiiGN_EPE96RJsB-wK3E5tlwbxK"

# Initialize Blynk
blynk = Blynk(BLYNK_AUTH)

# Initialize I2C LCD (Address 0x27 or 0x3F, check using `i2cdetect -y 1`)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, backlight_enabled=True)

# Function to receive text from Blynk (V1) and display on LCD
@blynk.on("V1")
def display_text(value):
    text = value[0][:16]  # Limit text to 16 characters
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string(text)
    print(f"LCD Updated: {text}")

# Function to handle connection
@blynk.on("connected")
def blynk_connected():
    print("Blynk Connected")

# Run Blynk
while True:
    blynk.run()
    time.sleep(0.1)
