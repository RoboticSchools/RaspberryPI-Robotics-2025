"""
Components Used:
- Raspberry Pi
- RGB LED (Common Cathode)
- Jumper Wires
- Breadboard
"""

import RPi.GPIO as gpio
import tkinter as tk

# Pin configuration
red_pin = 21   # GPIO21 connected to Red pin of RGB LED
green_pin = 20  # GPIO20 connected to Green pin of RGB LED
blue_pin = 16  # GPIO16 connected to Blue pin of RGB LED

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(red_pin, gpio.OUT)  # Set Red pin as output
gpio.setup(green_pin, gpio.OUT)  # Set Green pin as output
gpio.setup(blue_pin, gpio.OUT)  # Set Blue pin as output

# Function to turn off all colors
def turn_off():
    gpio.output(red_pin, gpio.LOW)
    gpio.output(green_pin, gpio.LOW)
    gpio.output(blue_pin, gpio.LOW)
    label.config(text="RGB LED OFF")

# Functions to control RGB LED colors
def red_on():
    turn_off()
    gpio.output(red_pin, gpio.HIGH)
    label.config(text="Red ON")

def green_on():
    turn_off()
    gpio.output(green_pin, gpio.HIGH)
    label.config(text="Green ON")

def blue_on():
    turn_off()
    gpio.output(blue_pin, gpio.HIGH)
    label.config(text="Blue ON")

def yellow_on():
    turn_off()
    gpio.output(red_pin, gpio.HIGH)
    gpio.output(green_pin, gpio.HIGH)
    label.config(text="Yellow ON")

def cyan_on():
    turn_off()
    gpio.output(green_pin, gpio.HIGH)
    gpio.output(blue_pin, gpio.HIGH)
    label.config(text="Cyan ON")

def magenta_on():
    turn_off()
    gpio.output(red_pin, gpio.HIGH)
    gpio.output(blue_pin, gpio.HIGH)
    label.config(text="Magenta ON")

def white_on():
    turn_off()
    gpio.output(red_pin, gpio.HIGH)
    gpio.output(green_pin, gpio.HIGH)
    gpio.output(blue_pin, gpio.HIGH)
    label.config(text="White ON")

# Create GUI window
window = tk.Tk()
window.title("RGB LED Controller")
window.geometry("500x500")

# Create a frame and pack it in the center
frame = tk.Frame(window)
frame.pack(expand=True)

# Button size settings
btn_width = 12
btn_height = 3

# Buttons arranged in a 4-row x 2-column grid (all with white text)
tk.Button(frame, text="Red", bg="red", fg="white", font=("Arial", 13), width=btn_width, height=btn_height, command=red_on).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Green", bg="green", fg="white", font=("Arial", 13), width=btn_width, height=btn_height, command=green_on).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Blue", bg="blue", fg="white", font=("Arial", 13), width=btn_width, height=btn_height, command=blue_on).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Yellow", bg="yellow", fg="black", font=("Arial", 13), width=btn_width, height=btn_height, command=yellow_on).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame, text="Cyan", bg="cyan", fg="black", font=("Arial", 13), width=btn_width, height=btn_height, command=cyan_on).grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame, text="Magenta", bg="magenta", fg="white", font=("Arial", 13), width=btn_width, height=btn_height, command=magenta_on).grid(row=2, column=1, padx=5, pady=5)
tk.Button(frame, text="White", bg="white", fg="black", font=("Arial", 13), width=btn_width, height=btn_height, command=white_on).grid(row=3, column=0, padx=5, pady=5)
tk.Button(frame, text="Turn Off", bg="gray", fg="white", font=("Arial", 13), width=btn_width, height=btn_height, command=turn_off).grid(row=3, column=1, padx=5, pady=5)

# Label to display current LED state (always black text)
label = tk.Label(frame, text="RGB LED OFF", font=("Arial", 13), fg="black")
label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
try:
    window.mainloop()
except KeyboardInterrupt:
    pass

gpio.cleanup()  # Reset GPIO settings before exiting

