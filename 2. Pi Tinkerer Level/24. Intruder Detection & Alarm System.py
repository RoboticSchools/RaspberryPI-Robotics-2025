"""
Components Used:
- Raspberry Pi
- PIR Motion Sensor
- Green LED (Safe Mode)
- Red LED (Intruder Alert)
- Buzzer (Alarm)
- Push Button (Stop Alarm)
- Resistors
- Breadboard
- Jumper Wires
"""

import RPi.GPIO as gpio
import time

# Pin configuration
pir_pin = 21       # GPIO21 connected to PIR sensor
button_pin = 20    # GPIO20 connected to Push Button (Stop Alarm)
buzzer_pin = 16    # GPIO16 connected to Buzzer (Alarm)
green_led = 5      # GPIO5 connected to Green LED (Safe Mode)
red_led = 6        # GPIO6 connected to Red LED (Intruder Alert)

# GPIO setup
gpio.setmode(gpio.BCM)  # Set pin numbering system to BCM
gpio.setup(pir_pin, gpio.IN)  # Set PIR sensor as input
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set Button as input with pull-up resistor
gpio.setup(buzzer_pin, gpio.OUT)  # Set Buzzer as output
gpio.setup(green_led, gpio.OUT)  # Set Green LED as output
gpio.setup(red_led, gpio.OUT)  # Set Red LED as output

try:
    while True:
        motion_state = gpio.input(pir_pin)  # Read PIR sensor value

        if motion_state == gpio.HIGH:  # Motion detected (Intruder Alert)
            gpio.output(green_led, gpio.LOW)  # Turn OFF Green LED (Safe Mode)
            gpio.output(red_led, gpio.HIGH)  # Turn ON Red LED (Intruder Alert)
            gpio.output(buzzer_pin, gpio.HIGH)  # Turn ON Buzzer (Alarm)
            print("Intruder Alert! Red LED & Buzzer ON")

            # Wait here until the button is pressed (Stop Alarm)
            while gpio.input(button_pin) == gpio.HIGH:
                time.sleep(0.1)  # Small delay to prevent excessive CPU usage

            # When button is pressed, stop the alarm
            gpio.output(buzzer_pin, gpio.LOW)  # Turn OFF Buzzer
            gpio.output(red_led, gpio.LOW)  # Turn OFF Red LED
            gpio.output(green_led, gpio.HIGH)  # Turn ON Green LED (Safe Mode)
            print("Alarm Stopped. System in Safe Mode.")

            while True:  # Halt execution, system stays in safe mode until restarted
                time.sleep(1)

        else:  # No motion detected (Safe Mode)
            gpio.output(green_led, gpio.HIGH)  # Ensure Green LED is ON
            print("No Motion Detected. Safe Mode.")

        time.sleep(0.1)  # Small delay for stable readings

except KeyboardInterrupt:
    pass

gpio.cleanup()  # Reset GPIO settings before exiting
