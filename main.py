import pyautogui
from time import sleep
import win32api 
import win32con

sleep(2)
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

while True:
    y_pos = 411
    if pyautogui.pixelMatchesColor(601,y_pos,(0, 0, 0)):
        click(601,y_pos)
    if pyautogui.pixelMatchesColor(684,y_pos,(0, 0, 0)):
        click(684,y_pos)
    if pyautogui.pixelMatchesColor(775,y_pos,(0, 0, 0)):
        click(775,y_pos)
    if pyautogui.pixelMatchesColor(859,y_pos,(0, 0, 0)):
        click(859,y_pos)