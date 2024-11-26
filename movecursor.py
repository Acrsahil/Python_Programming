import pyautogui
import time
import os


def on_move(x,y):
    os.system("python test.py")
    # print(f"your current pointer is x = {x} , y = {y}")

prev_x, prev_y = pyautogui.position()

while True:
    current_x, current_y = pyautogui.position()

    if (current_x != prev_x or current_y != prev_y):
        on_move(current_x,current_y)  # Call the function to print "Hello"
        prev_x, prev_y = current_x, current_y  # Update the previous position
    time.sleep(0.1)
