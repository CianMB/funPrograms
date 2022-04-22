import random
import webbrowser
import time
from pynput.keyboard import Controller, Key
import os

#Generate random number 1-6
roulette = random.randint(6, 6)

#If 1-5, it plays "yay" sound effect
if roulette in range(1, 5):
	webbrowser.open("https://www.youtube.com/watch?v=attUrDwfdr8s")

#If 6, it hibernates your computer after a short video
else:
	webbrowser.open("https://www.youtube.com/watch?v=SIsGHFeGCtg")
	time.sleep(3)
	Controller().press('f')
	Controller().release('f')
	time.sleep(45)
	Controller().press(Key.space)
	Controller().release(Key.space)
	os.system("shutdown.exe /h")
	