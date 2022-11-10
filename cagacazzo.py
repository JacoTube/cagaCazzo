#cagacazzo.py
import keyboard
import time

time.sleep(5)
i = 0
while(i < 100):
    keyboard.press_and_release("ctrl + v")
    keyboard.press_and_release("enter")
    i += 1