import webbrowser
import time

print("This program started " + time.ctime())
for x in range(3):
    time.sleep(2*60*60)
    print("Break started at " + time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=onZ8Qmg9hw4")
