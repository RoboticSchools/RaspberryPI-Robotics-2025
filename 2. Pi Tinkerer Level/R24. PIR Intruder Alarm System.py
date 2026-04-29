"""
Components Used:
1. Raspberry Pi
2. PIR Motion Sensor
3. Green LED
4. Red LED
5. Buzzer
6. Push Button
7. Breadboard
8. Jumper Wires
"""

import RPi.GPIO as gpio
import time

pir_pin = 21      # GPIO pin for PIR sensor
button_pin = 16   # GPIO pin for button
buzzer_pin = 12   # GPIO pin for buzzer
green_led = 23    # GPIO pin for green LED
red_led = 24      # GPIO pin for red LED

gpio.setmode(gpio.BCM)            # Use BCM pin numbering
gpio.setup(pir_pin, gpio.IN)      # Set PIR as input
gpio.setup(button_pin, gpio.IN, pull_up_down=gpio.PUD_UP)  # Set button as input
gpio.setup(buzzer_pin, gpio.OUT)  # Set buzzer as output
gpio.setup(green_led, gpio.OUT)   # Set green LED as output
gpio.setup(red_led, gpio.OUT)     # Set red LED as output

try:
    while True:
        motion_state = gpio.input(pir_pin)  # Read PIR sensor

        if motion_state == 1:  # Motion detected
            gpio.output(green_led, gpio.LOW)
            gpio.output(red_led, gpio.HIGH)     # Turn red LED ON
            gpio.output(buzzer_pin, gpio.HIGH)  # Turn buzzer ON
            print("Intruder Alert!")

            while gpio.input(button_pin) == 0:  # Wait for button press
                time.sleep(0.1)

            gpio.output(buzzer_pin, gpio.LOW)  # Turn buzzer OFF
            gpio.output(red_led, gpio.LOW)     # Turn red LED OFF
            print("Alarm Stopped")
            time.sleep(5)

        else:
            gpio.output(green_led, gpio.HIGH)  # Turn green LED ON
            print("Safe Mode")

        time.sleep(0.1)  # Small delay

except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit