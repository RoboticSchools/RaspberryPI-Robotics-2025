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
pwm = gpio.PWM(led_pin, 1000) # Create PWM (1000 Hz)
pwm.start(0)                  # Start with LED OFF

def turn_on():
    pwm.ChangeDutyCycle(100)              # Full brightness
    label_status.configure(text="Status: ON")  # Update label

def turn_off():
    pwm.ChangeDutyCycle(0)                # LED OFF
    label_status.configure(text="Status: OFF") # Update label

def handle_entry():
    text = entry_box.get().lower()  # Get input
    if text == "on":
        turn_on()
    elif text == "off":
        turn_off()
    else:
        label_status.configure(text="Invalid Input")
    entry_box.delete(0, "end")  # Clear entry

def radio_control():
    if radio_var.get() == 1:
        turn_on()
    else:
        turn_off()

def set_brightness(val):
    pwm.ChangeDutyCycle(int(val))  # Set brightness
    label_status.configure(text=f"Brightness: {int(val)}%")

ctk.set_appearance_mode("light")  # Set theme
ctk.set_default_color_theme("blue")

window = ctk.CTk()  # Create window
window.title("LED Controller")
window.geometry("500x550")

frame = ctk.CTkFrame(window)  # Main frame
frame.pack(expand=True, fill="both", padx=20, pady=20)

button_frame = ctk.CTkFrame(frame)
button_frame.pack(pady=15)

button_on = ctk.CTkButton(button_frame, text="ON", command=turn_on,
                          width=120, height=40)  # ON button
button_on.pack(side="left", padx=15)

button_off = ctk.CTkButton(button_frame, text="OFF", command=turn_off,
                           fg_color="red", hover_color="#cc0000",
                           width=120, height=40)  # OFF button
button_off.pack(side="left", padx=15)

radio_var = ctk.IntVar(value=0)  # Store radio value

radio_frame = ctk.CTkFrame(frame)
radio_frame.pack(pady=15)

radio_on = ctk.CTkRadioButton(radio_frame, text="ON", variable=radio_var,
                              value=1, command=radio_control)  # ON radio
radio_on.pack(side="left", padx=15)

radio_off = ctk.CTkRadioButton(radio_frame, text="OFF", variable=radio_var,
                               value=0, command=radio_control)  # OFF radio
radio_off.pack(side="left", padx=15)

entry_box = ctk.CTkEntry(frame, placeholder_text="Enter ON / OFF",
                         width=200)  # Input box
entry_box.pack(pady=15)

submit_button = ctk.CTkButton(frame, text="SUBMIT",
                              command=handle_entry)  # Submit button
submit_button.pack(pady=15)

slider = ctk.CTkSlider(frame, from_=0, to=100,
                       command=set_brightness)  # Brightness slider
slider.pack(pady=15)

label_status = ctk.CTkLabel(frame, text="Waiting for Input")  # Status label
label_status.pack(pady=15)

try:
    window.mainloop()  # Run GUI
except KeyboardInterrupt:
    pwm.stop()  # Stop PWM
    gpio.cleanup()  # Reset GPIO