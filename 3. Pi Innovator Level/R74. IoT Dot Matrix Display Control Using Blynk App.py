"""
Components Used:
- Raspberry Pi
- MAX7219 LED Matrix Display
- Blynk App
- Jumper Wires
"""

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT
from BlynkLib import Blynk

# Blynk authentication token
BLYNK_AUTH = "Your_Blynk_Auth_Token"

# Initialize Blynk
blynk = Blynk(BLYNK_AUTH)

# Initialize MAX7219 LED Matrix
serial = spi(port=0, device=0, gpio=None)
device = max7219(serial, cascaded=1, block_orientation=90)

# Function to display message received from Blynk
@blynk.on("V1")  # Virtual pin V1 for message input
def display_message(value):
    message = value[0]
    show_message(device, message, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)

# Run Blynk in a loop
try:
    while True:
        blynk.run()

except KeyboardInterrupt:
    print("Exiting program.")
