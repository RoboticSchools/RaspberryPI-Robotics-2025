"""
Components Used:
- Raspberry Pi
- OLED Display (128x64) using SSD1306
- DHT11 Sensor
- LDR (Light Dependent Resistor)
- PIR Motion Sensor
- Jumper Wires
"""

import time
import Adafruit_SSD1306
import RPi.GPIO as GPIO
import Adafruit_DHT
from PIL import Image, ImageDraw, ImageFont

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

# Initialize DHT11 sensor
DHT_PIN = 4
sensor = Adafruit_DHT.DHT11

# Initialize PIR sensor
PIR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# LDR Pin
LDR_PIN = 18
GPIO.setup(LDR_PIN, GPIO.IN)

# Function to read DHT11 sensor
def read_dht11():
    humidity, temperature = Adafruit_DHT.read(sensor, DHT_PIN)
    return temperature, humidity

# Function to read LDR (Light sensor)
def read_ldr():
    return GPIO.input(LDR_PIN)

# Function to read PIR (Motion sensor)
def read_pir():
    return GPIO.input(PIR_PIN)

# Function to display sensor data on OLED
def display_sensor_data():
    # Read sensor data
    temperature, humidity = read_dht11()
    ldr_status = "Light" if read_ldr() else "Dark"
    pir_status = "Motion Detected" if read_pir() else "No Motion"

    draw.rectangle((0, 0, width, height), outline=0, fill=0)  # Clear display

    # Display Temperature and Humidity
    if temperature is not None and humidity is not None:
        draw.text((0, 0), f"Temp: {temperature}C", font=font, fill=255)
        draw.text((0, 10), f"Humidity: {humidity}%", font=font, fill=255)
    else:
        draw.text((0, 0), "Failed to read DHT11", font=font, fill=255)

    # Display LDR Status
    draw.text((0, 20), f"LDR: {ldr_status}", font=font, fill=255)

    # Display PIR Status
    draw.text((0, 30), f"PIR: {pir_status}", font=font, fill=255)

    # Update the display
    disp.image(image)
    disp.display()

# Continuously update sensor data on OLED
try:
    while True:
        display_sensor_data()
        time.sleep(2)  # Update every 2 seconds

except KeyboardInterrupt:
    disp.clear()
    disp.display()
    GPIO.cleanup()
    print("Exiting program.")
