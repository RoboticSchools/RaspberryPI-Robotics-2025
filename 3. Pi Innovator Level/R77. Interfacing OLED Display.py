"""
Components Used:
1. Raspberry Pi
2. OLED Display (128x64, SSD1306 I2C)
3. Jumper Wires

Install Required Library:
pip install adafruit-circuitpython-ssd1306 pillow --break-system-packages
"""

# Import required libraries
import time
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)  # initialize I2C communication

# OLED setup
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)  # initialize OLED display

oled.fill(0)  # clear display
oled.show()   # update display

# Create image buffer
width, height = oled.width, oled.height
image = Image.new("1", (width, height))  # create blank image (1-bit)
draw = ImageDraw.Draw(image)  # create drawing object

# Load font
font = ImageFont.load_default()  # load default font

# Draw text on image
draw.text((10, 20), "Hello, Raspberry Pi!", font=font, fill=255)

# Display on OLED
oled.image(image)  # send image to display
oled.show()        # update display

# Keep message visible for 5 seconds
time.sleep(5)