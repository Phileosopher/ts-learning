# Text 9 - green. Find green pixels. verified 2015-11-26
# set and get pixel. save

from Glib import *

startdraw(640, 480)
im = loadImage ("../07images/eclipse.gif")
for i in range(0, Width()):
    for j in range(0, Height()):
        c = getpixel(im, i,j)
        if green(c)>(red(c)+20) and green(c)>(blue(c)+20):
            setpixel (im, i, j, cvtColor3 (0,0,0))
        else:
            setpixel (im, i, j, cvtColor3(255,255,255))
image (im, 0, 0)
save (im, "out.gif")
enddraw()
