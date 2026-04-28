import RPi.GPIO as gpio
import customtkinter as ctk

led_pin = 21  # GPIO pin for LED

gpio.setmode(gpio.BCM)       # Use BCM pin numbering
gpio.setup(led_pin, gpio.OUT)  # Set LED as output

def led_on():
    gpio.output(led_pin, gpio.HIGH)  # Turn LED ON
    label.configure(text="LED is ON")  # Update label

def led_off():
    gpio.output(led_pin, gpio.LOW)   # Turn LED OFF
    label.configure(text="LED is OFF")  # Update label

ctk.set_appearance_mode("light")  # Set theme
ctk.set_default_color_theme("blue")

window = ctk.CTk()  # Create window
window.title("LED Controller")
window.geometry("500x300")

button_on = ctk.CTkButton(window, text="LED ON", command=led_on, width=200, height=50)  # ON button
button_on.pack(pady=20)

button_off = ctk.CTkButton(window, text="LED OFF", command=led_off, fg_color="red", hover_color="#cc0000", width=200, height=50)  # OFF button
button_off.pack(pady=20)

label = ctk.CTkLabel(window, text="LED is OFF", font=("Arial", 16))  # Status label
label.pack(pady=10)

try:
    window.mainloop()  # Run GUI
except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit