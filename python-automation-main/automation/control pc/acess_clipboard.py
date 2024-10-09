import pyautogui
import pyperclip

position = pyautogui.position()
print(position)

pyautogui.doubleClick(2228, 243)
pyautogui.hotkey("ctrl","a")
pyautogui.hotkey("ctrl","c")

text = pyperclip.paste()
pyautogui.alert(text)
print(text)