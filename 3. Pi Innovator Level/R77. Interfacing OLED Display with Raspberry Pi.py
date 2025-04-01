"""
Components Used:
- Raspberry Pi
- OLED Display (128x64) using SSD1306
- Jumper Wires
"""

import time
import Adafruit_SSD1306
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

# Draw some text
draw.text((0, 0), 'Hello Raspberry Pi!', font=font, fill=255)

# Display the image on the OLED
disp.image(image)
disp.display()

time.sleep(5)
