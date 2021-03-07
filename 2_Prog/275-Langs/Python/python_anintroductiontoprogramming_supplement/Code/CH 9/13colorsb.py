from Glib import *

startdraw(300, 300)
background(255)
strokeweight (10)
stroke (255, 0, 0, 65)
for i in range(0,300,20):
    line (0, i, width, i)
stroke (0,0,255,60)
for i in range (0, 300, 20):
    line (i, 0, i, height)
enddraw()
