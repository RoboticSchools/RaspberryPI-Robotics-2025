import time
import threading
from pynput import keyboard
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas

# Initialize LED Matrix
device = max7219(spi(port=0, device=0, gpio=None), cascaded=1, block_orientation=90)

position, direction, running, caught = 3, 1, True, False  # Initial states

def on_press(key):
    global running, caught
    if hasattr(key, 'char'):
        if key.char == "c":
            print("Caught the pixel! 🎯") if position == 3 else print("Missed! Try again.")
            caught, running = (position == 3), False
        elif key.char == "q":
            print("Game exited.")
            running = False

def move_dot():
    global position, direction
    while running:
        with canvas(device) as draw:
            draw.point((position, 3), fill="white")
        time.sleep(0.15)
        direction *= -1 if position in (0, 7) else 1
        position += direction

def play_game():
    print("Press 'c' to catch, 'q' to quit.")
    keyboard.Listener(on_press=on_press).start()
    move_dot()
    print("Game Over: You won!" if caught else "Game Over: You quit or missed.")

print("Press 's' to start the game.")
with keyboard.Listener(on_press=lambda key: play_game() if getattr(key, 'char', '') == 's' else None) as listener:
    listener.join()
