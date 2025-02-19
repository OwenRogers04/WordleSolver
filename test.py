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
    used = open("info/used.txt", 'r')
    possible = open("info/possible.txt", 'w')
    mylist = []
    for word in used:
        mylist.append(word[:5].strip().lower())
    
    dataframe1 = pd.DataFrame(mylist, columns=["word"])
    dataframe1.to_csv('info/possible.csv', index=False)




def preStart():
    findPossible()

def main():
    preStart()

if __name__=="__main__":
    main()