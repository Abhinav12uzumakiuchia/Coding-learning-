# clock
seconds = 00
minutes = 30
hours = 7
import time
from turtle import*
setup()
t1 = Turtle()
while True:
    t1.clear()
    t1.write(str(hours).zfill(2)+ ":"+ str(minutes).zfill(2)+":"+str(seconds).zfill(2),font = ("arial",30,"italic"))
    seconds = seconds + 1
    time.sleep(1)
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    if minutes == 60:
        minutes = 0
        hours = hours +1
