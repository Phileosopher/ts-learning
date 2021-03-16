# Test 10 - Threshold an image. verified 2015-11-26
# grey

from Glib import *

def draw ():
    global T, im
    for i in range(0, Width()):
        for j in range(0, Height()):
            c = getpixel(im, i,j)
            g = grey (c)
            if g < T:
                setpixel (im, i, j, cvtColor3 (0,0,0))
            else:
                setpixel (im, i, j, cvtColor3(255,255,255))
    image  (im, 0, 0)
    save (im, "thresh.jpg")
    noloop()

startdraw(640, 480)
im = loadImage ("images/eclipse.gif")
T = 128
enddraw()