"""
Components Used:
1. Raspberry Pi
2. Ultrasonic Sensor (HC-SR04)
3. Breadboard
4. Jumper Wires
"""

import time
import RPi.GPIO as gpio

# ---------------- GPIO Setup ----------------
trig_pin = 21  # trigger pin
echo_pin = 20  # echo pin

gpio.setmode(gpio.BCM)        # use BCM numbering
gpio.setup(trig_pin, gpio.OUT)
gpio.setup(echo_pin, gpio.IN)

# ---------------- Distance Function ----------------
def get_distance():
    gpio.output(trig_pin, False)
    time.sleep(0.05)  # allow sensor to settle

    # send 10µs trigger pulse
    gpio.output(trig_pin, True)
    time.sleep(0.00001)
    gpio.output(trig_pin, False)

    start_time = time.time()
    stop_time = time.time()

    # wait for echo to go HIGH
    while gpio.input(echo_pin) == 0:
        start_time = time.time()

    # wait for echo to go LOW
    while gpio.input(echo_pin) == 1:
        stop_time = time.time()

    # calculate distance in cm
    duration = stop_time - start_time
    distance = (duration * 34300) / 2  # speed of sound

    return round(distance, 2)

# ---------------- Main Loop ----------------
try:
    while True:
        distance = get_distance()        # read distance
        print(f"Distance: {distance} cm")
        time.sleep(1)                   # delay between readings

except KeyboardInterrupt:
    gpio.cleanup()  # reset GPIO