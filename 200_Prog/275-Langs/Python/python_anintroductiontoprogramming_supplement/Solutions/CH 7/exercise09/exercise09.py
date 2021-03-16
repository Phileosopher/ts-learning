# Exercise 8 - Identify red pixels
from Glib import *

s = imageSize("digit.gif")
startdraw(s[0], s[1])
fill (128)
im = loadImage ("digit.gif")
image (im, 0, 0)
nofill()
for i in range (0, Width()):
    for j in range (0, Height()):
        c = getpixel (im, i, j)
        if red(c)==255 and green(c)==0 and blue(c)==0:
            ellipse (i, j, 10, 10)
            print ("Red pixel at ", i, j)
enddraw()