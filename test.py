import webbrowser
import pyautogui
import time
import pandas as pd

def moveToStart():
    webbrowser.open('https://www.nytimes.com/games/wordle/index.html')
    time.sleep(2)

    location = pyautogui.locateOnScreen('images/play.png')
    pyautogui.click(location)
    time.sleep(1)

    location = pyautogui.locateOnScreen('images/X.png')
    pyautogui.click(location)
    time.sleep(.5)

    pyautogui.scroll(-500)

def findPossible():
    valid = pd.read_csv("info/valid-words.csv")
    possible = pd.read_csv("info/possible.csv")
    final = []

    for word in valid:
        if word not in possible:
            print(word + "\n")




def preStart():
    findPossible()

def main():
    preStart()

if __name__=="__main__":
    main()