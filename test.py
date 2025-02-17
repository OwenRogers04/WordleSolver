import webbrowser
import pyautogui
import time

webbrowser.open('https://www.nytimes.com/games/wordle/index.html')

print(pyautogui.__version__)

time.sleep(5)

location = pyautogui.locateOnScreen('play.png')
if location:
    pyautogui.click(location)