"""
Components Used:
- Raspberry Pi
- Pi DC Motor HAT
- Robot Car setup
- 4 DC Motors (Right Front, Right Back, Left Front, Left Back)
"""

import tkinter as tk
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import atexit

mh = Raspi_MotorHAT(addr=0x6f)

right_front = mh.getMotor(1)
right_back  = mh.getMotor(2)
left_front  = mh.getMotor(3)
left_back   = mh.getMotor(4)

speed = 150
right_front.setSpeed(speed)
right_back.setSpeed(speed)
left_front.setSpeed(speed)
left_back.setSpeed(speed)

def stop_motors():
    right_front.run(Raspi_MotorHAT.RELEASE)
    right_back.run(Raspi_MotorHAT.RELEASE)
    left_front.run(Raspi_MotorHAT.RELEASE)
    left_back.run(Raspi_MotorHAT.RELEASE)

def move_forward():
    right_front.run(Raspi_MotorHAT.FORWARD)
    right_back.run(Raspi_MotorHAT.FORWARD)
    left_front.run(Raspi_MotorHAT.FORWARD)
    left_back.run(Raspi_MotorHAT.FORWARD)

def move_backward():
    right_front.run(Raspi_MotorHAT.BACKWARD)
    right_back.run(Raspi_MotorHAT.BACKWARD)
    left_front.run(Raspi_MotorHAT.BACKWARD)
    left_back.run(Raspi_MotorHAT.BACKWARD)

def turn_left():
    right_front.run(Raspi_MotorHAT.FORWARD)
    right_back.run(Raspi_MotorHAT.FORWARD)
    left_front.run(Raspi_MotorHAT.BACKWARD)
    left_back.run(Raspi_MotorHAT.BACKWARD)

def turn_right():
    right_front.run(Raspi_MotorHAT.BACKWARD)
    right_back.run(Raspi_MotorHAT.BACKWARD)
    left_front.run(Raspi_MotorHAT.FORWARD)
    left_back.run(Raspi_MotorHAT.FORWARD)

# safe shutdown
atexit.register(stop_motors)

root = tk.Tk()
root.title("Robot Control")

# ---- Button with press + release ----
def make_button(text, row, col, press_func):
    btn = tk.Button(root, text=text, width=8, height=2)
    btn.grid(row=row, column=col, padx=10, pady=10)
    btn.bind("<ButtonPress-1>", lambda e: press_func())
    btn.bind("<ButtonRelease-1>", lambda e: stop_motors())
    return btn

make_button("Up", 0, 1, move_forward)
make_button("Left", 1, 0, turn_left)
make_button("Right", 1, 2, turn_right)
make_button("Down", 2, 1, move_backward)

# ---- Keyboard bindings ----
def on_key_press(event):
    key = event.keysym
    if key == "Up":
        move_forward()
    elif key == "Down":
        move_backward()
    elif key == "Left":
        turn_left()
    elif key == "Right":
        turn_right()

def on_key_release(event):
    stop_motors()

root.bind("<KeyPress>", on_key_press)
root.bind("<KeyRelease>", on_key_release)

# ensure motors stop when window is closed
def on_close():
    stop_motors()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
