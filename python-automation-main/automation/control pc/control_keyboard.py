import pyautogui
import time

def position_while():
    while True:
        position = pyautogui.position()
        print(position)

position = pyautogui.position()
print(position)

pyautogui.doubleClick(118,235)
time.sleep(2)
pyautogui.press("down")
pyautogui.press("enter")
pyautogui.write("Python automation\n")

pyautogui.hotkey("ctrl","a")
pyautogui.hotkey("ctrl","c")
pyautogui.press("down")
pyautogui.hotkey("ctrl","v")

pyautogui.press(["down","down"])
pyautogui.press(5*["down"])