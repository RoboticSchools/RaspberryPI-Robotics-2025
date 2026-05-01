"""
Components Used:
1. Raspberry Pi
2. OLED Display (128x64, SSD1306 I2C)
3. Jumper Wires

Install Required Library:
pip install adafruit-circuitpython-ssd1306 pillow psutil --break-system-packages
"""

# Import required libraries
import time
import board
import busio
import psutil
import subprocess
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# ---------------- I2C Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)

# ---------------- OLED Setup ----------------
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.show()

# ---------------- Create Image Buffer ----------------
width, height = oled.width, oled.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)

# ---------------- Load Font ----------------
font = ImageFont.load_default()

# ---------------- Get CPU Temperature ----------------
def get_cpu_temp():
    try:
        temp = subprocess.check_output(["vcgencmd", "measure_temp"]).decode()
        return temp.replace("temp=", "").replace("'C\n", "")
    except:
        return "N/A"

# ---------------- Get System Stats ----------------
def get_stats():
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    battery = psutil.sensors_battery()
    battery = battery.percent if battery else "N/A"

    temp = get_cpu_temp()

    return cpu, ram, disk, battery, temp

# ---------------- Display Dashboard ----------------
def display_stats():
    cpu, ram, disk, battery, temp = get_stats()

    # Clear screen
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Title
    draw.text((25, 0), "Pi Monitor", font=font, fill=255)

    # Left column
    draw.text((0, 16), f"CPU: {cpu}%", font=font, fill=255)
    draw.text((0, 28), f"RAM: {ram}%", font=font, fill=255)
    draw.text((0, 40), f"DSK: {disk}%", font=font, fill=255)

    # Right column
    draw.text((64, 16), f"TMP:{temp}C", font=font, fill=255)
    draw.text((64, 28), f"BAT:{battery}", font=font, fill=255)

    # Update OLED
    oled.image(image)
    oled.show()

# ---------------- Main Loop ----------------
try:
    while True:
        display_stats()
        time.sleep(2)

except KeyboardInterrupt:
    oled.fill(0)
    oled.show()
    print("Exiting...")