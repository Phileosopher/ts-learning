# Test 10 - Threshold an image. verified 2015-11-26
# grey
from Glib import *

startdraw(640, 480)
im = loadImage ("../07images/eclipse.gif")
T = 128
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
enddraw()