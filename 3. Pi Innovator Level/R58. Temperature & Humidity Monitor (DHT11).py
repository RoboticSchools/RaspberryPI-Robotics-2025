"""
Components Used:
1. Raspberry Pi
2. DHT11 Sensor (Temperature & Humidity)
3. LCD Display with I2C
4. Breadboard
5. Jumper Wires
"""

import adafruit_dht
from RPLCD.i2c import CharLCD
import time
import board

# ---------------- Sensor Setup ----------------
dht_sensor = adafruit_dht.DHT11(board.D17)  # DHT11 on GPIO17

# ---------------- LCD Setup ----------------
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)

# ---------------- Main Loop ----------------
try:
    while True:
        temperature = dht_sensor.temperature  # read temperature
        humidity = dht_sensor.humidity        # read humidity

        lcd.clear()

        if temperature is not None and humidity is not None:
            lcd.cursor_pos = (0, 0)
            lcd.write_string(f"Temp: {temperature}C")

            lcd.cursor_pos = (1, 0)
            lcd.write_string(f"Humidity: {humidity}%")
        else:
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Sensor Error")

        time.sleep(2)  # update delay

except KeyboardInterrupt:
    print("Exiting...")
    dht_sensor.exit()
    lcd.clear()