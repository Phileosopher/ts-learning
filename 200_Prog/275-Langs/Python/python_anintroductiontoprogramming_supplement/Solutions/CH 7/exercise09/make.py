# Set up the digit image
from Glib import *

red = cvtColor3(255, 0, 0)
s = imageSize("digit.gif")
startdraw(s[0], s[1])
im = loadImage ("digit.gif")
setpixel(im, 100, 110, red)   # Change the coordinates here
setpixel (im, 271, 300, red)
setpixel (im, 21, 439, red)
setpixel (im, 320, 240, red)
image (im, 0, 0)
save (im, "out.gif")
enddraw()
