"""
Components Used:
1. Raspberry Pi
2. LED
3. Breadboard
4. Jumper Wires

Install Required Library:
pip install customtkinter --break-system-packages
"""

import RPi.GPIO as gpio  # GPIO control
import customtkinter as ctk  # GUI library

led_pin = 21  # LED connected pin

# GPIO setup
gpio.setmode(gpio.BCM)  # Use BCM numbering
gpio.setup(led_pin, gpio.OUT)  # Set LED as output

# PWM setup for brightness
pwm = gpio.PWM(led_pin, 1000)  # 1kHz PWM
pwm.start(0)  # Start OFF

# Turn LED ON
def turn_on():
    pwm.ChangeDutyCycle(100)
    label_status.configure(text="Status: ON")

# Turn LED OFF
def turn_off():
    pwm.ChangeDutyCycle(0)
    label_status.configure(text="Status: OFF")

# Entry input handler
def handle_entry(event=None):
    text = entry_box.get().lower()
    if text == "on": turn_on()
    elif text == "off": turn_off()
    else: label_status.configure(text="Invalid Input")
    entry_box.delete(0, "end")

# Radio control
def radio_control():
    turn_on() if radio_var.get() == 1 else turn_off()

# Brightness control
def set_brightness(val):
    pwm.ChangeDutyCycle(int(val))
    label_status.configure(text=f"Brightness: {int(val)}%")

# Window setup
window = ctk.CTk()
window.title("LED Controller")
window.geometry("500x600")

frame_color = "#d9d9d9"  # Same color for all frames

# Main frame
frame = ctk.CTkFrame(window, fg_color=frame_color); frame.pack(expand=True, fill="both", padx=25, pady=25)

# Buttons
button_frame = ctk.CTkFrame(frame, fg_color=frame_color); button_frame.pack(pady=25)
button_on = ctk.CTkButton(button_frame, text="ON", command=turn_on, fg_color="green", font=("Arial", 15), width=150, height=45); button_on.pack(side="left", padx=20)
button_off = ctk.CTkButton(button_frame, text="OFF", command=turn_off, fg_color="red", font=("Arial", 15), width=150, height=45); button_off.pack(side="left", padx=20)

# Radio buttons
radio_var = ctk.IntVar(value=0)
radio_frame = ctk.CTkFrame(frame, fg_color=frame_color); radio_frame.pack(pady=25)
radio_on = ctk.CTkRadioButton(radio_frame, text="ON", variable=radio_var, value=1, command=radio_control, font=("Arial", 15)); radio_on.pack(side="left", padx=25)
radio_off = ctk.CTkRadioButton(radio_frame, text="OFF", variable=radio_var, value=0, command=radio_control, font=("Arial", 15)); radio_off.pack(side="left", padx=25)

# Entry input
entry_box = ctk.CTkEntry(frame, placeholder_text="Enter ON / OFF", font=("Arial", 15), width=260, height=40); entry_box.pack(pady=25); entry_box.bind("<Return>", handle_entry)

# Brightness slider
slider = ctk.CTkSlider(frame, from_=0, to=100, width=300, command=set_brightness); slider.pack(pady=25)

# Status label
label_status = ctk.CTkLabel(frame, text="Waiting for Input", font=("Arial", 15)); label_status.pack(pady=25)

# Run app
try:
    window.mainloop()
except KeyboardInterrupt:
    pwm.stop()
    gpio.cleanup()