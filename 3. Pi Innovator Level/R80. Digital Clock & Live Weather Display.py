"""
Components Used:
1. Raspberry Pi
2. OLED Display (128x64, SSD1306 I2C)
3. Internet (Weather API)
4. Jumper Wires

Install Required Library:
pip install adafruit-circuitpython-ssd1306 pillow requests --break-system-packages
"""

# Import required libraries
import time
import board
import busio
import requests
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# ---------------- API Setup ----------------
API_KEY = "YOUR_API_KEY"
CITY = "Bangalore"

# ---------------- OLED Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.show()

# ---------------- Image Buffer ----------------
width, height = oled.width, oled.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# ---------------- Weather Function ----------------
def get_weather():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=5)
        data = response.json()

        return data["main"]["temp"], data["main"]["humidity"], data["weather"][0]["main"]
    except:
        return "Err", "Err", "NoNet"

# ---------------- Initial Weather ----------------
temp, hum, cond = get_weather()
last_weather_update = time.time()

# ---------------- Main Loop ----------------
try:
    print("Clock + Weather Dashboard Started...")

    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%d-%m-%Y")

        # Update weather every 30 seconds
        if time.time() - last_weather_update > 30:
            temp, hum, cond = get_weather()
            last_weather_update = time.time()

        # Clear screen
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        # Display time and date
        draw.text((0, 0), "Time: " + current_time, font=font, fill=255)
        draw.text((0, 12), "Date: " + current_date, font=font, fill=255)

        # Display weather
        draw.text((0, 28), "Temp: " + str(temp) + " C", font=font, fill=255)
        draw.text((0, 40), "Hum: " + str(hum) + " %", font=font, fill=255)
        draw.text((0, 52), str(cond), font=font, fill=255)

        oled.image(image)
        oled.show()

        time.sleep(1)  # update every second

except KeyboardInterrupt:
    oled.fill(0)
    oled.show()
    print("Exiting...")