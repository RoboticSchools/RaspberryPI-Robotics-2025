"""
Components Used:
- Raspberry Pi
- RGB LED (Common Cathode)
- Blynk App (Menu Widget)
- Jumper Wires
- Breadboard
"""

import RPi.GPIO as gpio
import BlynkLib
import time

# Blynk authentication token (replace with your actual token)
BLYNK_AUTH = "35MM8LiiGN_EPE96RJsB-wK3E5tlwbxK"

# Pin configuration
red_pin = 21   # GPIO21 connected to Red LED
green_pin = 20 # GPIO20 connected to Green LED
blue_pin = 16  # GPIO16 connected to Blue LED

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(red_pin, gpio.OUT)   # Set Red LED pin as output
gpio.setup(green_pin, gpio.OUT) # Set Green LED pin as output
gpio.setup(blue_pin, gpio.OUT)  # Set Blue LED pin as output

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Function to set RGB LED color
def set_color(r, g, b, color_name):
    gpio.output(red_pin, r)
    gpio.output(green_pin, g)
    gpio.output(blue_pin, b)
    print(f"{color_name} LED ON")

# Menu widget handler (V1)
@blynk.on("V1")
def menu_handler(value):
    selection = int(value[0])  # Get selected menu option
    
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

# Function to handle connection
@blynk.on("connected")
def blynk_connected():
    print("Blynk Connected")

# Run Blynk
while True:
    blynk.run()
    time.sleep(0.1)
