import webbrowser
import pyautogui
import time

webbrowser.open('https://www.nytimes.com/games/wordle/index.html')

time.sleep(2)

location = pyautogui.locateOnScreen('images/play.png')
if location is None:
    print("Image not found on screen.")
else:
    pyautogui.click(location)

time.sleep(.5)

location = pyautogui.locateOnScreen('images/X.png')
if location is None:
    print("Image not found on screen.")
else:
    pyautogui.click(location)

time.sleep(.5)

pyautogui.scroll(-500)

time.sleep(.5)

pyautogui.typewrite('arose')
