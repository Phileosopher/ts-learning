# Test 5 - Pie chart 2016-07-19
# mod to background, arc
from Glib import *
from math import *

title = "Grades for Art 315"
ncategories = 6
maxsize = 20
hlabel = "Grade"
vlabel = "Number"
val = (2, 1, 4, 15, 10, 5)
lab = ("Other", "F", "D", "C", "B", "A")

def label (xx, yy, r, s, a1, ap):
    angle = a1 + ap/2
    d = r*1.25
    y = -sin (angle*3.1415/180.) * d + yy
    x = cos (angle*3.1415/180.) * d + xx
    text (s, x, y)

def pull (x, y, a1, ap):
    angle = a1 + ap/2
    d = 12
    y = -sin (angle*3.1415/180.) * d + y
    x = cos (angle*3.1415/180.) * d + x
    arc (x-150, y-150, x+150, y+150, a1, ap, Pieslice)


startdraw (600, 600)
background(180)
strokeweight (2)
fill (255)
textsize (24)
text (title, 120, 80)

r = 255
fill (r, 200, 200)
totalSize = 0
for i in range (0,ncategories):
        totalSize = totalSize + val[i]
anglePerCount = 360.0/totalSize
angle = 0
for i in range(0, ncategories):
        span = val[i]*anglePerCount
        if i == 3:
            pull(300, 300, angle, span)
        else:
            arc (150, 150, 450, 450, angle, span, PIESLICE)
        fill (255)
        label (300, 300, 150, lab[i], angle, span)
        angle = angle + span
        r = r - 20
        fill (r, 200, 200)
enddraw()
