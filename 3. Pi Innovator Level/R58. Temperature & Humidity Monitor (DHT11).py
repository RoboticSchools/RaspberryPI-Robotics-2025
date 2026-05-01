"""
Components Used:
1. Raspberry Pi
2. DHT11 Sensor (Temperature & Humidity)
3. LCD Display with I2C
4. Breadboard
5. Jumper Wires

Install Required Libraries (one line):
pip3 install adafruit-circuitpython-dht RPLCD smbus2 adafruit-blinka --break-system-packages
"""

import adafruit_dht
from RPLCD.i2c import CharLCD
import time
import board

# ---------------- Sensor Setup ----------------
dht_sensor = adafruit_dht.DHT11(board.D17)  # DHT11 connected to GPIO17

# ---------------- LCD Setup ----------------
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)  # 16x2 LCD

# ---------------- Main Loop ----------------
try:
    while True:
        # Read temperature and humidity from DHT11
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity

        lcd.clear()  # Clear display before updating

        # Check if sensor returned valid values
        if temperature is not None and humidity is not None:
            # Display temperature on first row
            lcd.cursor_pos = (0, 0)
            lcd.write_string(f"Temp: {temperature}C")

            # Display humidity on second row
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f"Humidity: {humidity}%")
        else:
            # If reading fails, show error message
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Sensor Error")

        time.sleep(2)  # Wait before next update

except KeyboardInterrupt:
    # Clean exit when program is stopped
    print("Exiting...")
    dht_sensor.exit()  # Release sensor
    lcd.clear()        # Clear LCD