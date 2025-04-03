"""
Components Used:
- Raspberry Pi
- MAX7219 LED Matrix Display
- Jumper Wires
"""

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT

# Initialize MAX7219 LED Matrix
serial = spi(port=0, device=0, gpio=None)
device = max7219(serial, cascaded=1, block_orientation=90)

# Continuous message display loop
try:
    while True:
        message = input("Enter message to display (or 'exit' to quit): ")
        if message.lower() == "exit":
            break
        
        # Display the message on LED matrix with scrolling effect
        show_message(device, message, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)

except KeyboardInterrupt:
    print("Exiting program.")
