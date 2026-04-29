"""
Components Used:
1. Raspberry Pi
2. LED
3. Breadboard
4. Jumper Wires

Install Required Library:
pip install customtkinter --break-system-packages
"""

import RPi.GPIO as gpio
import customtkinter as ctk

led_pin = 21  # GPIO pin for LED

gpio.setmode(gpio.BCM)        # Use BCM pin numbering
gpio.setup(led_pin, gpio.OUT) # Set LED as output

def led_on():
    gpio.output(led_pin, gpio.HIGH)  # Turn LED ON
    label.configure(text="LED is ON")  # Update label

def led_off():
    gpio.output(led_pin, gpio.LOW)   # Turn LED OFF
    label.configure(text="LED is OFF")  # Update label

window = ctk.CTk()  # Create window
window.title("LED Controller")
window.geometry("500x320")

# ON button
button_on = ctk.CTkButton(window,text="LED ON",command=led_on,fg_color="green",font=("Arial", 18),width=200,height=50)
button_on.pack(pady=20)

# OFF button
button_off = ctk.CTkButton(window,text="LED OFF",command=led_off,fg_color="red",font=("Arial", 18),width=200,height=50)
button_off.pack(pady=20)

# Status label
label = ctk.CTkLabel(window,text="LED is OFF",font=("Arial", 18))
label.pack(pady=10)

try:
    window.mainloop()  # Run GUI
except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit