# Test 03 gradient verified 2015-11-26
#line, point, Width, Height, omitting initialize
from Glib import *

def draw():
    global blue, delta
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

startdraw(400, 400)
enddraw()