import pyautogui
from time import sleep
import win32api 
import win32con
import keyboard
sleep(2)
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

while not keyboard.is_pressed('q'):
    y_pos = 411
    x_pos = [601,684,775,859]
    for x in x_pos:
        if pyautogui.pixelMatchesColor(x,y_pos,(0,0,0)):
            click(x, y_pos)
