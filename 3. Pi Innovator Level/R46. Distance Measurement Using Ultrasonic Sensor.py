"""
Components Used:
- Raspberry Pi
- Ultrasonic Sensor (HC-SR04)
- Breadboard
- Jumper Wires
"""

import time
import RPi.GPIO as gpio

# GPIO Pin configuration
trig_pin = 23  # Trigger pin connected to GPIO23
echo_pin = 24  # Echo pin connected to GPIO24

# GPIO setup
gpio.setmode(gpio.BCM)
gpio.setup(trig_pin, gpio.OUT)  # Set trig as output
gpio.setup(echo_pin, gpio.IN)   # Set echo as input

def get_distance():
    """Measure the distance using the ultrasonic sensor."""
    
    # Send a short pulse to trigger the sensor
    gpio.output(trig_pin, True)
    time.sleep(0.00001)  # 10µs pulse
    gpio.output(trig_pin, False)

    # Wait for the echo pin to go HIGH
    while gpio.input(echo_pin) == 0:
        start_time = time.time()

    # Wait for the echo pin to go LOW
    while gpio.input(echo_pin) == 1:
        end_time = time.time()

    # Calculate the distance in cm
    duration = end_time - start_time
    distance = (duration * 34300) / 2  # Speed of sound = 343m/s

    return round(distance, 2)  # Return the distance rounded to 2 decimal places

try:
    while True:
        distance = get_distance()
        print(f"Distance: {distance} cm")
        time.sleep(1)  # Delay between readings

except KeyboardInterrupt:
    print("Exiting...")
    gpio.cleanup()
