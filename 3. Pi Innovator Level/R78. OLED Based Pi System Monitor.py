"""
Components Used:
1. Raspberry Pi
2. OLED Display (128x64, SSD1306 I2C)
3. Jumper Wires
"""

import time
import board
import busio
import psutil
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
image = Image.new("1", (width, height))  # blank image
draw = ImageDraw.Draw(image)  # draw object
font = ImageFont.load_default()  # load font

# get system stats
def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)  # CPU usage
    memory = psutil.virtual_memory().percent  # RAM usage
    return cpu, memory

# display stats
def display_stats():
    cpu, memory = get_system_stats()  # read stats

    draw.rectangle((0, 0, width, height), outline=0, fill=0)  # clear screen

    draw.text((0, 0), f"CPU: {cpu}%", font=font, fill=255)  # show CPU
    draw.text((0, 20), f"RAM: {memory}%", font=font, fill=255)  # show RAM

    oled.image(image)  # send image
    oled.show()        # update display

# main loop
try:
    while True:
        display_stats()  # update stats
        time.sleep(2)    # delay

except KeyboardInterrupt:
    oled.fill(0)  # clear display
    oled.show()
    print("Exiting...")