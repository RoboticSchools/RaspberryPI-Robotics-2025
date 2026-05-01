"""
Components Used:
1. Raspberry Pi
2. MAX7219 LED Matrix Display
3. Jumper Wires

Install Required Library:
pip install luma.led_matrix luma.core pillow --break-system-packages
"""

# Import required libraries
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT
import time

# ---------------- SPI Setup (Pi 5 FIX) ----------------
serial_interface = spi(port=0, device=0, gpio=noop())

# ---------------- LED Matrix Setup ----------------
led_matrix = max7219(serial_interface, cascaded=1, block_orientation=90)

# ---------------- Main Loop ----------------
try:
    while True:
        message = input("Enter message (type 'exit' to quit): ")

        if message.lower() == "exit":
            break

        show_message(led_matrix, message, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Exiting...")