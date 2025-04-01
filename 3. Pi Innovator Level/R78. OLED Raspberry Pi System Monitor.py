"""
Components Used:
- Raspberry Pi
- OLED Display (128x64) using SSD1306
- Jumper Wires
"""

import time
import Adafruit_SSD1306
import psutil
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO

# Initialize the display
disp = Adafruit_SSD1306.SSD1306_128_64(rst=24)

# Initialize library
disp.begin()

# Clear the display
disp.clear()
disp.display()

# Create an image buffer
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Create a drawing object
draw = ImageDraw.Draw(image)

# Load a font
font = ImageFont.load_default()

# Function to get system stats
def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)  # Get CPU usage percentage
    memory = psutil.virtual_memory().percent  # Get memory usage percentage
    return cpu, memory

# Function to display system stats on OLED
def display_stats():
    cpu, memory = get_system_stats()

    draw.rectangle((0, 0, width, height), outline=0, fill=0)  # Clear display

    # Display CPU usage
    draw.text((0, 0), f"CPU: {cpu}% ", font=font, fill=255)

    # Display memory usage
    draw.text((0, 20), f"RAM: {memory}% ", font=font, fill=255)

    # Update the display
    disp.image(image)
    disp.display()

# Continuously update stats on OLED
try:
    while True:
        display_stats()
        time.sleep(2)  # Update every 2 seconds

except KeyboardInterrupt:
    disp.clear()
    disp.display()
    print("Exiting program.")
