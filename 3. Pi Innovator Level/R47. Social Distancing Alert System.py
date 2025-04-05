"""
Components Used:
- Raspberry Pi
- Ultrasonic Sensor
- Red LED
- Green LED
- Buzzer
- Breadboard
- Jumper Wires
"""

import time
import RPi.GPIO as gpio

# GPIO Pin configuration
trig = 23      # Trigger pin of HC-SR04
echo = 24      # Echo pin of HC-SR04
red_led = 12   # Red LED pin
green_led = 16 # Green LED pin
buzzer = 21    # Buzzer pin

# GPIO setup
gpio.setmode(gpio.BCM)
gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)
gpio.setup(red_led, gpio.OUT)
gpio.setup(green_led, gpio.OUT)
gpio.setup(buzzer, gpio.OUT)

def get_distance():
    """Measure the distance using the ultrasonic sensor."""
    
    # Send a short pulse to trigger the sensor
    gpio.output(trig, True)
    time.sleep(0.00001)  # 10µs pulse
    gpio.output(trig, False)

    # Wait for the echo pin to go HIGH
    start_time = time.time()
    while gpio.input(echo) == 0:
        start_time = time.time()

    # Wait for the echo pin to go LOW
    end_time = time.time()
    while gpio.input(echo) == 1:
        end_time = time.time()

    # Calculate the distance in cm
    duration = end_time - start_time
    distance = (duration * 34300) / 2  # Speed of sound = 343m/s

    return round(distance, 2)  # Return the distance rounded to 2 decimal places

try:
    while True:
        distance = get_distance()
        print(f"Distance: {distance} cm")

        # Control LEDs and buzzer based on distance
        if distance < 30:
            gpio.output(red_led, True)
            gpio.output(green_led, False)
            gpio.output(buzzer, True)
        else:
            gpio.output(red_led, False)
            gpio.output(green_led, True)
            gpio.output(buzzer, False)

        time.sleep(0.1)  # Update every 100ms

except KeyboardInterrupt:
    print("Exiting...")
    gpio.cleanup()
