"""
Components Used:
- Raspberry Pi
- LED
- Jumper Wires
- Breadboard
"""

import RPi.GPIO as gpio
import tkinter as tk

# Pin configuration
led_pin = 21

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(led_pin, gpio.OUT)

# Function to turn LED ON
def led_on():
    gpio.output(led_pin, gpio.HIGH)
    label.config(text="LED is ON")

# Function to turn LED OFF
def led_off():
    gpio.output(led_pin, gpio.LOW)
    label.config(text="LED is OFF")

# Create GUI window
window = tk.Tk()
window.title("LED Controller")
window.geometry("500x300")

# LED control buttons (same size)
button_on = tk.Button(window, text="LED ON", bg="#b4dd1e", font=("Arial", 15), relief="flat", command=led_on, width=15, height=2)
button_on.pack(pady=20)

button_off = tk.Button(window, text="LED OFF", bg="#ff4444", font=("Arial", 15), relief="flat", command=led_off, width=15, height=2)
button_off.pack(pady=20)

# LED status label
label = tk.Label(window, text="LED is OFF", font=("Arial", 13))
label.pack(pady=10)

# Run the Tkinter event loop
try:
    window.mainloop()
except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings before exiting
