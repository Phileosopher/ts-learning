# Test 03 gradient verified 2016-07-19
#line, point, Width, Height, omitting initialize
from Glib import *

startdraw(400, 400)
background (255)
delta = 127.0/Height()
blue = 255
for y in range (0, Height()):
    yy = Height()-y
#        stroke (100, 100, blue)
    fill (100, 100, blue)
    for x in range(0, Width()):
        point (x, yy)
#       line (0, yy, Width(), yy)
    blue = blue - delta

enddraw()