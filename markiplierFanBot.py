#Markiplier Fan Bot
#Checks video inputted to see if it is made by Markiplier
#If not, it spams something like, "THIS IS NOT MARKIPLIER!!! DEATH FALL UPON YOU!!!!"
#Then terminates
#If it is, it opens a window with that video
#Fullscreens it
#Then disables your keyboard and mouse until it's over

import pafy
import webbrowser
import time
from pynput.keyboard import Controller as kb
from pynput.mouse import Controller as ms
import keyboard

#Pafify turns a video URL just it's video ID, making it viable
#to become a pafy object
def pafify(videoURL):
    pafificatedURL = videoURL[32:]
    return pafificatedURL

def markCheck(defaultURL, pafifiedURL):
    if pafifiedURL.author == "Markiplier":
        for i in range(1, 100):
            print("HOLY SHIT IT'S FUCKING MARKIPLIER!!!")
        webbrowser.open(defaultURL)
        time.sleep(3)
        kb().press('f')
        kb().release('f')

        currentPlaytime = 0

        while currentPlaytime < pafifiedURL.length:
            for i in range(150):
                keyboard.block_key(i)
            ms().position = (1300, 800)
            time.sleep(1)
            currentPlaytime += 1
        if currentPlaytime == pafifiedURL.length:
            quit()
    else:
        for i in range(1, 100):
            print("THIS ISN'T MARKIPLIER!!! I'M GONNA\nKILL MYSELF!!!!")
        time.sleep(5)
        quit()

inputVideo = input("Please enter a video URL: ")
baptVid = pafify(inputVideo)
pafyVideo = pafy.new(baptVid)

markCheck(inputVideo, pafyVideo)