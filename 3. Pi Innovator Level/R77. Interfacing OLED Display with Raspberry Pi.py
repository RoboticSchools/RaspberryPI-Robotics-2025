"""
Components Used:
- Raspberry Pi
- OLED Display (128x64) using SSD1306 (I2C)
- Jumper Wires
"""

import time
import board
import busio
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

# Draw text
draw.text((10, 20), "Hello, Raspberry Pi!", font=font, fill=255)

# Display the image on the OLED
oled.image(image)
oled.show()

time.sleep(5)  # Display for 5 seconds
