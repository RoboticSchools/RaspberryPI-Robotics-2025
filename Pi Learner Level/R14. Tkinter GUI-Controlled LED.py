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
led_pin = 21  # GPIO21 connected to LED

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(led_pin, gpio.OUT)  # Set LED pin as output

# Function to turn LED ON
def led_on():
    gpio.output(led_pin, gpio.HIGH)
    label.config(text="LED is ON", fg="green")

# Function to turn LED OFF
def led_off():
    gpio.output(led_pin, gpio.LOW)
    label.config(text="LED is OFF", fg="red")

# Create GUI window
window = tk.Tk()
window.title("LED Controller")
window.geometry("500x400")

# LED control buttons
button_on = tk.Button(window, text="LED ON", bg="#b4dd1e", font=("Century Gothic", 15), relief="flat", command=led_on)
button_on.pack(pady=20, ipadx=10, ipady=10)

button_off = tk.Button(window, text="LED OFF", bg="#ff4444", font=("Century Gothic", 15), relief="flat", command=led_off)
button_off.pack(pady=20, ipadx=10, ipady=10)

# LED status label
label = tk.Label(window, text="LED is OFF", font=("Century Gothic", 13), fg="red")
label.pack(pady=10)

# Run the Tkinter event loop
try:
    window.mainloop()
except KeyboardInterrupt:
    pass

gpio.cleanup()  # Reset GPIO settings before exiting
