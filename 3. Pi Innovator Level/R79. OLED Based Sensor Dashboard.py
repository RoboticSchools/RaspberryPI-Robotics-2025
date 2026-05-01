"""
Components Used:
1. Raspberry Pi
2. OLED Display (128x64, SSD1306 I2C)
3. LDR Sensor (Digital Output)
4. PIR Motion Sensor
5. DHT11 Sensor
6. Jumper Wires

Install Required Library:
pip install adafruit-circuitpython-ssd1306 pillow adafruit-circuitpython-dht RPi.GPIO --break-system-packages
"""

# Import required libraries
import time
import board
import busio
import RPi.GPIO as gpio
import adafruit_dht
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# ---------------- GPIO Setup ----------------
gpio.setmode(gpio.BCM)  # use BCM numbering

ldr_pin = 21  # LDR pin
pir_pin = 23  # PIR sensor pin

gpio.setup(ldr_pin, gpio.IN)  # LDR input
gpio.setup(pir_pin, gpio.IN)  # PIR input

# ---------------- DHT11 Setup ----------------
dht = adafruit_dht.DHT11(board.D17)

# ---------------- OLED Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# ---------------- Create Image Buffer ----------------
width, height = oled.width, oled.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)

# ---------------- Load Font ----------------
font = ImageFont.load_default()

# ---------------- Main Loop ----------------
try:
    while True:
        # Read LDR
        ldr_state = gpio.input(ldr_pin)
        light_status = "Dark" if ldr_state == 1 else "Light"

        # Read PIR
        pir_state = gpio.input(pir_pin)
        motion_status = "Motion" if pir_state == 1 else "No Motion"

        # Read DHT11
        try:
            temp = dht.temperature
            hum = dht.humidity
        except RuntimeError:
            temp = "Err"
            hum = "Err"

        # Clear display buffer
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        # Display data
        draw.text((0, 0), f"LDR: {light_status}", font=font, fill=255)
        draw.text((0, 15), f"PIR: {motion_status}", font=font, fill=255)
        draw.text((0, 30), f"Temp: {temp}C", font=font, fill=255)
        draw.text((0, 45), f"Hum: {hum}%", font=font, fill=255)

        # Update OLED
        oled.image(image)
        oled.show()

        time.sleep(2)

except KeyboardInterrupt:
    oled.fill(0)
    oled.show()
    gpio.cleanup()
    print("Exiting...")