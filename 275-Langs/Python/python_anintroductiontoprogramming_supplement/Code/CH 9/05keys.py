from Glib import *
from random import *

def keyPressed (k):
    if k == K_PLUS:
        ellipse (randrange(0,width), randrange(0,height), 30, 30)

startdraw(400, 400)
fill (200, 0, 0)
background (200)
enddraw()
