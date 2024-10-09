import pyautogui

position = pyautogui.position()
print(position)

pyautogui.move(100,0,duration=1)
pyautogui.moveTo(139,280,duration=1)
pyautogui.click()
pyautogui.click(clicks=2)
pyautogui.doubleClick()

#WINDOWS
pyautogui.click(139,280)
pyautogui.click(139,280,button="right")

#MAC
pyautogui.click(139,280)
pyautogui.dragTo(139,280,button="right")