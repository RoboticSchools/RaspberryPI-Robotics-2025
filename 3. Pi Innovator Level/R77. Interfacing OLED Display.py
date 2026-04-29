"""
Components Used:
1. Raspberry Pi
2. OLED Display (128x64, SSD1306 I2C)
3. Jumper Wires
"""

import time
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)  # init I2C

# OLED setup
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)  # init display

oled.fill(0)  # clear display
oled.show()

# create image buffer
width, height = oled.width, oled.height
image = Image.new("1", (width, height))  # create blank image
draw = ImageDraw.Draw(image)  # draw object

# load font
font = ImageFont.load_default()  # default font

# draw text
draw.text((10, 20), "Hello, Raspberry Pi!", font=font, fill=255)  # add text

# display on OLED
oled.image(image)  # send image
oled.show()        # update display

time.sleep(5)  # wait 5 seconds