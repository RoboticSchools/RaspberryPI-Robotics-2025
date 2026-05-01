"""
Components Used:
1. Raspberry Pi
2. I2C LCD Display (16x2)
3. Jumper Wires

Install Required Library:
pip install RPLCD smbus2 --break-system-packages

Note:
Check I2C address using:
i2cdetect -y 1

Common addresses:
0x27 or 0x3F
"""

import customtkinter as ctk
import time
from RPLCD.i2c import CharLCD

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, cols=16, rows=2)

# Create main window
app = ctk.CTk()
app.geometry("600x200")
app.configure(fg_color="#D3D3D3")  # light grey background

# Variables to store selected row and direction
row_var = ctk.StringVar(value="0")      # 0 = first row, 1 = second row
dir_var = ctk.StringVar(value="left")   # default direction

# Frame to hold all widgets
frame = ctk.CTkFrame(app, fg_color="#D3D3D3")
frame.pack(pady=30)

# Entry box for user to type text
entry = ctk.CTkEntry(frame, width=300, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=2, pady=15)

# Button to choose row (first or second)
ctk.CTkSegmentedButton(frame, values=["First Row", "Second Row"], command=lambda v: row_var.set("0" if v == "First Row" else "1"), font=("Arial", 18)).grid(row=1, column=0, padx=10)

# Button to choose scroll direction (left or right)
ctk.CTkSegmentedButton(frame, values=["Left", "Right"], command=lambda v: dir_var.set(v.lower()),font=("Arial", 18)).grid(row=1, column=1, padx=10)

# Function to scroll text on LCD
def scroll_text(text, row, direction):
    # Add spaces before and after text for smooth scrolling
    text = " " * 16 + text + " " * 16

    # Loop through text and display 16 characters at a time
    for i in range(len(text) - 15):
        lcd.cursor_pos = (row, 0)  # set position on LCD

        # If direction is left → normal scrolling
        # If direction is right → reverse scrolling trick
        if direction == "left":
            lcd.write_string(text[i:i+16])
        else:
            lcd.write_string(text[::-1][i:i+16][::-1])

        app.update()     # keep GUI responsive
        time.sleep(0.3)  # control speed

# When Enter key is pressed
entry.bind("<Return>", lambda e: (lcd.clear(), scroll_text(entry.get(), int(row_var.get()), dir_var.get())))

# Run the GUI
app.mainloop()