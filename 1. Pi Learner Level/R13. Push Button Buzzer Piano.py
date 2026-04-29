"""
Components Used:
1. Raspberry Pi
2. Buzzer
3. 4 Push Buttons
4. Breadboard
5. Jumper Wires
"""

import RPi.GPIO as gpio
import time

buzzer_pin = 21                 # GPIO pin for buzzer
button_pins = [26, 19, 13, 6]  # GPIO pins for buttons

notes = [262, 294, 330, 349]  # Note frequencies

gpio.setmode(gpio.BCM)  # Use BCM pin numbering
gpio.setup(buzzer_pin, gpio.OUT)  # Set buzzer as output
gpio.setup(button_pins, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set buttons as input

buzzer = gpio.PWM(buzzer_pin, 1)  # Create PWM object

try:
    while True:
        for i, button in enumerate(button_pins):
            if gpio.input(button) == 0:  # Check button press
                buzzer.ChangeFrequency(notes[i])  # Set frequency
                buzzer.start(50)  # Start buzzer
                print(f"Button {i+1} Pressed - {notes[i]} Hz")
                time.sleep(0.2)  # Small delay
                buzzer.stop()  # Stop buzzer

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit