"""
Components Used:
- Raspberry Pi
- OLED Display (128x64) using SSD1306 (I2C)
- Jumper Wires
"""

import time
import board
import busio
import psutil
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Initialize I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Create SSD1306 display object
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear the display
oled.fill(0)
oled.show()

# Create an image buffer
width = oled.width
height = oled.height
image = Image.new("1", (width, height))
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
    draw.text((0, 0), f"CPU: {cpu}%", font=font, fill=255)

    # Display memory usage
    draw.text((0, 20), f"RAM: {memory}%", font=font, fill=255)

    # Update the display
    oled.image(image)
    oled.show()

# Continuously update stats on OLED
try:
    while True:
        display_stats()
        time.sleep(2)  # Update every 2 seconds

except KeyboardInterrupt:
    oled.fill(0)
    oled.show()
    print("Exiting program.")
