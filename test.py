import webbrowser
import pyautogui
import time
import pandas as pd

def moveToStart():
    webbrowser.open('https://www.nytimes.com/games/wordle/index.html')
    time.sleep(2)

    location = pyautogui.locateOnScreen('images/play.png')
    pyautogui.click(location)
    time.sleep(.5)

    location = pyautogui.locateOnScreen('images/X.png')
    pyautogui.click(location)
    time.sleep(.5)

    pyautogui.scroll(-500)

def findPossible():
    
def preStart():
    findPossible()
    moveToStart()

def main():
    preStart()

if __name__=="__main__":
    main()