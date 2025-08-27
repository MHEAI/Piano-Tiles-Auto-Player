import pyautogui
from time import sleep
sleep(2)


while True:
    y_pos = 411
    if pyautogui.pixelMatchesColor(601,y_pos,(0, 0, 0)):
        pyautogui.click(601,y_pos)
    if pyautogui.pixelMatchesColor(684,y_pos,(0, 0, 0)):
        pyautogui.click(684,y_pos)
    if pyautogui.pixelMatchesColor(775,y_pos,(0, 0, 0)):
        pyautogui.click(775,y_pos)
    if pyautogui.pixelMatchesColor(859,y_pos,(0, 0, 0)):
        pyautogui.click(859,y_pos)