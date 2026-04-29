"""
Components Used:
1. Raspberry Pi
2. MAX7219 LED Matrix Display
3. Blynk App
4. Jumper Wires
"""

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT
from BlynkLib import Blynk

# Blynk setup
BLYNK_AUTH = "Your_Blynk_Auth_Token"  # auth token
blynk = Blynk(BLYNK_AUTH)  # init Blynk

# LED matrix setup
serial_interface = spi(port=0, device=0, gpio=None)  # SPI init
led_matrix = max7219(serial_interface, cascaded=1, block_orientation=90)  # display init

# receive message from Blynk
@blynk.on("V1")
def display_message(value):
    message = value[0]  # get message
    show_message(led_matrix, message, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)  # scroll text

# main loop
try:
    print("Blynk LED Matrix Started...")

    while True:
        blynk.run()  # handle Blynk events

except KeyboardInterrupt:
    print("Exiting...")