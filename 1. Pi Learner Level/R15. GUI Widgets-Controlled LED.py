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
pwm = gpio.PWM(led_pin, 1000)  # Set PWM frequency to 1000 Hz
pwm.start(0)  # Start PWM with 0% duty cycle (LED OFF)

# Function to turn LED ON
def turn_on():
    pwm.ChangeDutyCycle(100)  # 100% brightness
    label_status.config(text="Status: ON", fg="black")

# Function to turn LED OFF
def turn_off():
    pwm.ChangeDutyCycle(0)  # 0% brightness (LED OFF)
    label_status.config(text="Status: OFF", fg="black")

# Function to handle entry input
def handle_entry():
    text = entry_box.get().strip().lower()
    if text == "on":
        turn_on()
    elif text == "off":
        turn_off()
    else:
        label_status.config(text="Invalid Input", fg="black")
    entry_box.delete(0, tk.END)  # Clear entry box

# Function to handle radio button selection
def radio_control():
    if radio_var.get() == 1:
        turn_on()
    else:
        turn_off()

# Function to handle slider value
def set_brightness(val):
    pwm.ChangeDutyCycle(int(val))
    label_status.config(text=f"Brightness: {val}%", fg="black")

# Create GUI window
window = tk.Tk()
window.title("LED Controller")
window.geometry("500x550")
window.configure(bg="#f0f0f0")

# Main frame for better layout
frame = tk.Frame(window, bg="#f0f0f0")
frame.pack(expand=True)

# Buttons (ON/OFF) in one row
button_frame = tk.Frame(frame, bg="#f0f0f0")
button_frame.pack(pady=15)

button_on = tk.Button(button_frame, text="ON", bg="#4CAF50", fg="white", font=("Arial", 13), relief="flat", command=turn_on, width=12, height=2)
button_on.pack(side="left", padx=15)

button_off = tk.Button(button_frame, text="OFF", bg="#F44336", fg="white", font=("Arial", 13), relief="flat", command=turn_off, width=12, height=2)
button_off.pack(side="left", padx=15)

# Radio Buttons (ON/OFF) in one row
radio_var = tk.IntVar()
radio_var.set(0)  # Default to OFF

radio_frame = tk.Frame(frame, bg="#f0f0f0")
radio_frame.pack(pady=15)

radio_on = tk.Radiobutton(radio_frame, text="ON", variable=radio_var, value=1, font=("Arial", 13), command=radio_control, bg="#f0f0f0")
radio_on.pack(side="left", padx=15)

radio_off = tk.Radiobutton(radio_frame, text="OFF", variable=radio_var, value=0, font=("Arial", 13), command=radio_control, bg="#f0f0f0")
radio_off.pack(side="left", padx=15)

# Entry box for input
entry_box = tk.Entry(frame, font=("Arial", 13), width=20, justify="center", relief="flat", bg="white", bd=1)
entry_box.pack(pady=15, ipady=8)

submit_button = tk.Button(frame, text="SUBMIT", bg="#007BFF", fg="white", font=("Arial", 13), relief="flat", command=handle_entry, width=12, height=2)
submit_button.pack(pady=15)

# Brightness control slider
slider = tk.Scale(frame, from_=0, to=100, orient="horizontal", font=("Arial", 13), length=300, command=set_brightness, bg="#f0f0f0", relief="flat")
slider.pack(pady=15, ipady=10)

# Status label
label_status = tk.Label(frame, text="Waiting for Input", font=("Arial", 13), fg="black", bg="#f0f0f0", relief="flat")
label_status.pack(pady=15)

# Run the Tkinter event loop
try:
    window.mainloop()
except KeyboardInterrupt:
    pass

# Cleanup GPIO on exit
pwm.stop()
gpio.cleanup()
