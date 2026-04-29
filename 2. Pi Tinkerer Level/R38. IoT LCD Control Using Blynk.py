"""
Components Used:
1. Raspberry Pi
2. I2C LCD Display (16x2)
3. Blynk App
4. Jumper Wires

Install Required Library:
pip install RPLCD smbus2 blynklib --break-system-packages

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

blynk = Blynk(BLYNK_AUTH)  # Initialize Blynk

# Initialize LCD
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)

# Receive text from Blynk (Virtual Pin V1)
@blynk.on("V1")
def display_text(value):
    text = value[0]  # Get full text

    lcd.clear()  # Clear screen

    # Split text into 2 lines (max 16 chars each)
    line1 = text[:16]
    line2 = text[16:32]

    lcd.cursor_pos = (0, 0)
    lcd.write_string(line1)

    lcd.cursor_pos = (1, 0)
    lcd.write_string(line2)

    print(f"LCD Updated: {text}")

# Blynk connection status
@blynk.on("connected")
def blynk_connected():
    print("Blynk Connected")

try:
    while True:
        blynk.run()        # Handle Blynk events
        time.sleep(0.05)   # Small delay

except KeyboardInterrupt:
    lcd.clear()  # Clear LCD on exit