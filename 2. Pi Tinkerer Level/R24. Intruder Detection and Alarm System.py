"""
Components Used:
- Raspberry Pi
- PIR Motion Sensor
- Green LED (Safe Mode)
- Red LED (Intruder Alert)
- Buzzer (Alarm)
- Push Button (Stop Alarm)
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
pir_pin = 21      
button_pin = 16  
buzzer_pin = 12  
green_led = 23 
red_led = 24

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(pir_pin, gpio.IN)  # Set PIR sensor as input
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set Button as input with pull-up resistor
gpio.setup(buzzer_pin, gpio.OUT)
gpio.setup(green_led, gpio.OUT)
gpio.setup(red_led, gpio.OUT) 

try:
    while True:
        motion_state = gpio.input(pir_pin)  # Read PIR sensor value

        if motion_state == 1:  # Motion detected (Intruder Alert)
            gpio.output(green_led, gpio.LOW) 
            gpio.output(red_led, gpio.HIGH)
            gpio.output(buzzer_pin, gpio.HIGH) 
            print("Intruder Alert! Red LED & Buzzer ON")

            # Wait here until the button is pressed (Stop Alarm)
            while gpio.input(button_pin) == 0:
                time.sleep(0.1)  # Small delay to prevent excessive CPU usage

            # When button is pressed, stop the alarm
            gpio.output(buzzer_pin, gpio.LOW)
            gpio.output(red_led, gpio.LOW)
            print("Alarm Stopped. System in Safe Mode.")
            time.sleep(5)

        else:  # No motion detected (Safe Mode)
            gpio.output(green_led, gpio.HIGH)
            print("No Motion Detected. Safe Mode.")

        time.sleep(0.1)  # Small delay for stable readings

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO settings before exiting
