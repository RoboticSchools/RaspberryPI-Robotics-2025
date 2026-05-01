"""
Components Used:
1. Raspberry Pi
2. I2C LCD Display (16x2)
3. Blynk WebApp
4. Jumper Wires

Install Required Library:
pip install RPLCD smbus2 blynk-library-python --break-system-packages

Note:
Check I2C address using:
i2cdetect -y 1

Common addresses:
0x27 or 0x3F
"""

import time
from BlynkLib import Blynk
from RPLCD.i2c import CharLCD

BLYNK_AUTH = "YOUR_BLYNK_AUTH_TOKEN"  # Add your Blynk token

blynk = Blynk(BLYNK_AUTH, server="blynk.cloud", port=80)  # Initialize Blynk

# Initialize LCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)

selected_row = 0  # Default row

# Receive text from Blynk (Virtual Pin V1)
def display_text(value):
    text = value[0]  # Get text

    if len(text) > 15:  # Validate length
        print("Error: Max 15 characters allowed")
        return

    lcd.clear()

    lcd.cursor_pos = (selected_row, 0)
    lcd.write_string(text)

    print(f"LCD Updated: {text}")

# Receive row selection from Blynk (Virtual Pin V2)
def row_select(value):
    global selected_row
    selected_row = int(value[0])  # 0 or 1
    print(f"Row Selected: {selected_row}")

# Blynk connection status
def blynk_connected():
    print("Blynk Connected")

# Bind handlers
blynk.on("V1", display_text)
blynk.on("V2", row_select)
blynk.on("connected", blynk_connected)

try:
    while True:
        blynk.run()        # Handle Blynk events
        time.sleep(0.05)   # Small delay

except KeyboardInterrupt:
    lcd.clear()  # Clear LCD on exit