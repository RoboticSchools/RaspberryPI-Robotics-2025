"""
Components Used:
- Raspberry Pi
- Buzzer
- 4 Push Buttons
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
buzzer_pin = 21
button_pins = [26, 19, 13, 6]  # GPIO pins connected to the buttons

# Frequencies for musical notes (C, D, E, F)
notes = [262, 294, 330, 349]  # Corresponding frequencies in Hz

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(buzzer_pin, gpio.OUT)
gpio.setup(button_pins, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set buttons as input with internal pull-up resistors

buzzer = gpio.PWM(buzzer_pin, 1)  # Initialize PWM on buzzer pin

try:
    while True:
        for i, button in enumerate(button_pins):
            if gpio.input(button) == 0:  # Check if button is pressed
                buzzer.ChangeFrequency(notes[i])  # Set buzzer frequency to note
                buzzer.start(50)  # Start buzzer with 50% duty cycle
                print(f"Button {i+1} Pressed - Playing Note {notes[i]} Hz")
                time.sleep(0.2)  # Debounce delay
                buzzer.stop()  # Stop buzzer after sound

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings on exit
