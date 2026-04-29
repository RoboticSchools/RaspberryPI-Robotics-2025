"""
Components Used:
1. Raspberry Pi
2. OLED Display (128x64, SSD1306 I2C)
3. LDR Sensor (Digital Output)
4. Ultrasonic Sensor (HC-SR04)
5. DHT11 Sensor
6. Jumper Wires
"""

import time
import board
import busio
import RPi.GPIO as GPIO
import adafruit_dht
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# ---------------- GPIO Setup ----------------
GPIO.setmode(GPIO.BCM)  # use BCM numbering

ldr_pin = 21  # LDR pin
trig = 23     # ultrasonic trigger
echo = 24     # ultrasonic echo

GPIO.setup(ldr_pin, GPIO.IN)  # LDR input
GPIO.setup(trig, GPIO.OUT)    # trigger output
GPIO.setup(echo, GPIO.IN)     # echo input

# ---------------- DHT11 Setup ----------------
dht = adafruit_dht.DHT11(board.D17)  # DHT11 pin

# ---------------- OLED Setup ----------------
i2c = busio.I2C(board.SCL, board.SDA)  # I2C init
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)  # display init

width, height = oled.width, oled.height  # screen size
image = Image.new("1", (width, height))  # create image
draw = ImageDraw.Draw(image)  # draw object
font = ImageFont.load_default()  # font

# ---------------- Ultrasonic Function ----------------
def get_distance():
    GPIO.output(trig, False)  # low trigger
    time.sleep(0.05)  # settle

    GPIO.output(trig, True)  # send pulse
    time.sleep(0.00001)
    GPIO.output(trig, False)

    start = time.time()
    stop = time.time()

    while GPIO.input(echo) == 0:
        start = time.time()  # wait HIGH

    while GPIO.input(echo) == 1:
        stop = time.time()  # wait LOW

    return round((stop - start) * 17150, 2)  # distance cm

# ---------------- Main Loop ----------------
try:
    print("Sensor Dashboard Started...")

    while True:
        ldr_state = GPIO.input(ldr_pin)  # read LDR

        light_status = "Dark" if ldr_state == 1 else "Light"  # LDR status

        distance = get_distance()  # ultrasonic distance

        temp = dht.temperature  # temperature
        hum = dht.humidity      # humidity

        draw.rectangle((0, 0, width, height), outline=0, fill=0)  # clear screen

        draw.text((0, 0), f"LDR: {light_status}", font=font, fill=255)  # show LDR
        draw.text((0, 15), f"Dist: {distance}cm", font=font, fill=255)  # show distance
        draw.text((0, 30), f"Temp: {temp}C", font=font, fill=255)  # show temp
        draw.text((0, 45), f"Hum: {hum}%", font=font, fill=255)  # show humidity

        oled.image(image)  # send image
        oled.show()        # update display

        time.sleep(2)  # delay

except KeyboardInterrupt:
    oled.fill(0)  # clear display
    oled.show()
    GPIO.cleanup()  # reset GPIO
    print("Exiting...")