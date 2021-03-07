# Test 8 - green  2015 Nov 26
# loadImage, image, initializing within main.
from Glib import *
im = None

def draw ():
    global im
    image (im, 0,0)

startdraw(640, 480)
im = loadImage ("images/eclipse.gif")
enddraw()