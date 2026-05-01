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
API_KEY = "YOUR_API_KEY"  # enter your OpenWeather API key
CITY = "Bangalore"        # set your city

# ---------------- I2C + OLED Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)  # initialize I2C
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)  # initialize OLED display

# ---------------- Create Image Buffer ----------------
width, height = oled.width, oled.height  # get display size
image = Image.new("1", (width, height))  # create blank image
draw = ImageDraw.Draw(image)  # create drawing object

# ---------------- Load Font ----------------
font = ImageFont.load_default()  # load default font

# ---------------- Function: Get Weather ----------------
def get_weather():
    # Create API request URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    # Fetch data from API
    data = requests.get(url).json()

    # Extract required values
    temp = data["main"]["temp"]          # temperature (°C)
    humidity = data["main"]["humidity"]  # humidity (%)
    condition = data["weather"][0]["main"]  # weather condition

    return temp, humidity, condition

# ---------------- Main Loop ----------------
try:
    print("Clock + Weather Dashboard Started...")

    while True:
        # Get current time and date
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%d-%m-%Y")

        # Get weather data
        try:
            temp, hum, cond = get_weather()
        except:
            temp, hum, cond = "Err", "Err", "No Net"

        # Clear previous screen
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        # Display time and date
        draw.text((0, 0), f"Time: {current_time}", font=font, fill=255)
        draw.text((0, 12), f"Date: {current_date}", font=font, fill=255)

        # Display weather data
        draw.text((0, 28), f"Temp: {temp}C", font=font, fill=255)
        draw.text((0, 40), f"Hum: {hum}%", font=font, fill=255)
        draw.text((0, 52), f"{cond}", font=font, fill=255)

        # Update OLED display
        oled.image(image)
        oled.show()

        time.sleep(10)  # refresh every 10 seconds

# Handle Ctrl + C safely
except KeyboardInterrupt:
    oled.fill(0)
    oled.show()
    print("Exiting...")