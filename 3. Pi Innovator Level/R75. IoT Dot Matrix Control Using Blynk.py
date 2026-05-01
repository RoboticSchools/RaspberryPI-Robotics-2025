"""
Components Used:
1. Raspberry Pi
2. MAX7219 LED Matrix Display
3. Blynk Web App
4. Jumper Wires

Install Required Library:
pip install luma.led_matrix luma.core pillow blynk-library-python --break-system-packages
"""

# Import required libraries
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT
from BlynkLib import Blynk
import time

# ---------------- Blynk Setup ----------------
BLYNK_AUTH = 'your_blynk_auth_token'  # Replace with your Blynk auth token
blynk = Blynk(BLYNK_AUTH, server="blynk.cloud", port=80)

# ---------------- LED Matrix Setup (Pi 5 FIX) ----------------
serial_interface = spi(port=0, device=0, gpio=noop())
led_matrix = max7219(serial_interface, cascaded=1, block_orientation=90)

# ---------------- Variable ----------------
message = ""

# ---------------- Handler Function (No Decorator) ----------------
def handle_v1(pin, value):
    global message
    message = value[0]

    show_message(led_matrix, message, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)

# Manually assign handler to Virtual Pin V1
blynk.handle_event("write V1", handle_v1)

# ---------------- Main Loop ----------------
try:
    while True:
        blynk.run()      # process Blynk events
        time.sleep(0.01) # small delay

except KeyboardInterrupt:
    print("Exiting...")