import RPi.GPIO as gpio
from BlynkLib import Blynk
import time

BLYNK_AUTH = "35MM8LiiGN_EPE96RJsB-wK3E5tlwbxK"  # Blynk auth token

red_pin = 21    # GPIO pin for red LED
green_pin = 20  # GPIO pin for green LED
blue_pin = 16   # GPIO pin for blue LED

gpio.setmode(gpio.BCM)           # Use BCM pin numbering
gpio.setup(red_pin, gpio.OUT)    # Set red pin as output
gpio.setup(green_pin, gpio.OUT)  # Set green pin as output
gpio.setup(blue_pin, gpio.OUT)   # Set blue pin as output

blynk = Blynk(BLYNK_AUTH)  # Initialize Blynk

def set_color(r, g, b, color_name):
    gpio.output(red_pin, r)    # Set red
    gpio.output(green_pin, g)  # Set green
    gpio.output(blue_pin, b)   # Set blue
    print(f"{color_name} LED ON")

@blynk.on("V1")
def menu_handler(value):
    selection = int(value[0])  # Get selected option

    if selection == 1:
        set_color(1, 0, 0, "Red")
    elif selection == 2:
        set_color(0, 1, 0, "Green")
    elif selection == 3:
        set_color(0, 0, 1, "Blue")
    elif selection == 4:
        set_color(1, 1, 0, "Yellow")
    elif selection == 5:
        set_color(0, 1, 1, "Cyan")
    elif selection == 6:
        set_color(1, 0, 1, "Magenta")
    elif selection == 7:
        set_color(1, 1, 1, "White")
    elif selection == 8:
        set_color(0, 0, 0, "LED OFF")

@blynk.on("connected")
def blynk_connected():
    print("Blynk Connected")  # Connection status

try:
    while True:
        blynk.run()  # Run Blynk
        time.sleep(0.1)  # Small delay

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit