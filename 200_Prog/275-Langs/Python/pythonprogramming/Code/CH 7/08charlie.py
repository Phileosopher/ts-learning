# Test 8 - charlie  2015 Nov 26
# loadImage, image, initializing within main.
from Glib import *
im = None

startdraw(640, 480)
im = loadImage ("../07images/charlie.gif")
image (im, 0,0)
enddraw()