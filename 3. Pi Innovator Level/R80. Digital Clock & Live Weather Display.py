"""
Components Used:
1. Raspberry Pi
2. OLED Display (128x64, SSD1306 I2C)
3. Internet (Weather API)
4. Jumper Wires
"""

import time
import board
import busio
import requests
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# ---------------- API Setup ----------------
API_KEY = "YOUR_API_KEY"  # add your API key
CITY = "Bangalore"        # change your city

# ---------------- I2C + OLED Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)  # init I2C
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)  # init OLED

width, height = oled.width, oled.height  # screen size
image = Image.new("1", (width, height))  # image buffer
draw = ImageDraw.Draw(image)  # draw object
font = ImageFont.load_default()  # font

# ---------------- Weather Function ----------------
def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"  # API URL
    data = requests.get(url).json()  # fetch data

    temp = data["main"]["temp"]  # temperature
    humidity = data["main"]["humidity"]  # humidity
    condition = data["weather"][0]["main"]  # weather type

    return temp, humidity, condition

# ---------------- Main Loop ----------------
try:
    print("Clock + Weather Dashboard Started...")

    while True:
        now = datetime.now()  # current time
        current_time = now.strftime("%H:%M:%S")  # format time
        current_date = now.strftime("%d-%m-%Y")  # format date

        temp, hum, cond = get_weather()  # get weather

        draw.rectangle((0, 0, width, height), outline=0, fill=0)  # clear screen

        draw.text((0, 0), f"Time: {current_time}", font=font, fill=255)  # show time
        draw.text((0, 12), f"Date: {current_date}", font=font, fill=255)  # show date

        draw.text((0, 28), f"Temp: {temp}C", font=font, fill=255)  # show temp
        draw.text((0, 40), f"Hum: {hum}%", font=font, fill=255)  # show humidity
        draw.text((0, 52), f"{cond}", font=font, fill=255)  # show condition

        oled.image(image)  # send image
        oled.show()        # update display

        time.sleep(10)  # update every 10 sec

except KeyboardInterrupt:
    oled.fill(0)  # clear display
    oled.show()
    print("Exiting...")