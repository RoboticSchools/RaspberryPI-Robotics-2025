import RPi.GPIO as gpio   # Library to control Raspberry Pi GPIO pins (input/output)

# --- Pin configuration ---
led_pin = 21  # The GPIO pin number (BCM mode) where the LED is connected

# --- GPIO setup ---
gpio.setmode(gpio.BCM)        # Set pin numbering system to BCM (Broadcom SOC channel)
gpio.setup(led_pin, gpio.OUT) # Configure the LED pin to work as an output

print("User Input Controlled LED Program Started (Type 'on', 'off', or 'exit')")

try:
    while True:
        # --- Ask the user for input ---
        command = input("Enter command: ").lower()

        # --- Control LED based on user input ---
        if command == "on":
            gpio.output(led_pin, gpio.HIGH)  # Send HIGH signal to turn the LED on
            print("LED is ON")

        elif command == "off":
            gpio.output(led_pin, gpio.LOW)   # Send LOW signal to turn the LED off
            print("LED is OFF")

        elif command == "exit":
            print("Exiting program...")
            break  # Exit the loop

        else:
            print("Invalid command. Please type 'on', 'off', or 'exit'.")

except KeyboardInterrupt:
    # --- Cleanup on exit ---
    print("\nProgram stopped by user. Cleaning up GPIO...")  
    gpio.cleanup()  # Reset all GPIO settings to safe state
