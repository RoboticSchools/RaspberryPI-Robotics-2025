import RPi.GPIO as gpio
from bluedot import BlueDot
from signal import pause

led_pin = 21  # GPIO pin for LED

gpio.setmode(gpio.BCM)       # Use BCM pin numbering
gpio.setup(led_pin, gpio.OUT)  # Set LED as output

bd = BlueDot()  # Create BlueDot object

def led_on():
    gpio.output(led_pin, gpio.HIGH)  # Turn LED ON
    print("LED ON - Button Pressed")

def led_off():
    gpio.output(led_pin, gpio.LOW)   # Turn LED OFF
    print("LED OFF - Button Released")

bd.when_pressed = led_on    # Run when button pressed
bd.when_released = led_off  # Run when button released

try:
    pause()  # Keep program running
except KeyboardInterrupt:
    gpio.cleanup()  # Reset GPIO on exit