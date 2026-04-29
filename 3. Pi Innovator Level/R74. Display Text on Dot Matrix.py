"""
Components Used:
1. Raspberry Pi
2. MAX7219 LED Matrix Display
3. Jumper Wires
"""

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT

# LED Matrix setup
serial_interface = spi(port=0, device=0, gpio=None)  # SPI init
led_matrix = max7219(serial_interface, cascaded=1, block_orientation=90)  # display init

# Main loop
try:
    print("LED Matrix Display Started...")

    while True:
        message = input("Enter message (type 'exit' to quit): ")  # user input

        if message.lower() == "exit":
            break  # stop program

        show_message(led_matrix, message, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)  # scroll text

except KeyboardInterrupt:
    print("Exiting...")