"""
Components Used:
- Raspberry Pi
- MAX7219 8x8 LED Matrix
- Jumper Wires
"""
from luma.core.interface.serial import spi
from luma.led_matrix.device import max7219
from time import sleep

# Initialize SPI connection to MAX7219
serial = spi(port=0, device=0, gpio=None)
device = max7219(serial, width=8, height=8)

# Function to display a string on the 8x8 Matrix
def display_text(text):
    device.clear()  # Clear the display
    device.text(text, 0, 0, fill="white")  # Display the string
    sleep(3)  # Display for 3 seconds
    device.clear()  # Clear the display after 3 seconds

# Main Program Loop
try:
    while True:
        # Take user input for the text to display
        text = input("Enter text to display (max 8 characters): ")
        
        # Ensure the text doesn't exceed 8 characters
        if len(text) > 8:
            print("Text is too long! Please enter up to 8 characters.")
            continue
        
        display_text(text)

except KeyboardInterrupt:
    device.clear()  # Ensure the display is cleared when exiting
    print("Exiting program...")
