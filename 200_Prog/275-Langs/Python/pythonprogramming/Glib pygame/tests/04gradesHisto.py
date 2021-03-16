# Test 04 histogram verified 2015-11-26
# Fonts, line thickness
from Glib import *

title = "Grades for Art 315"
ncategories = 6
maxsize = 20
hlabel = "Grade"
vlabel = "Number of Students"
val = (2, 1, 4, 15, 10, 5)
lab = ("Other", "F", "D", "C", "B", "A")

def verticalLabel(v):
    lasti = 0
    x = 12
    y = 200
    for i in range(0, len(v)):
        if (v[i] == " "):
            text (v[lasti:i], x, y)
            y = y + 40
            lasti = i
    text (v[lasti:], x, y)

def draw ():
    background(180)
    setfont("times")
    strokeweight (5)
    line (100, 100, 100, 500)
    line (100, 500, 500, 500)

    textsize (24)
    text (title, 120, 80)
    textsize (14)
    cx = (400-len(hlabel)*14)/2
    text (hlabel, 100+cx, 580)

    verticalLabel(vlabel)
    wid = (400-10)/ncategories
    ht = 390.0/maxsize
    strokeweight (1)
    fill (200, 50, 200)
    rectmode (CORNER)
    for i in range(0,ncategories):
        ulx = 100 + i*wid+2
        uly = 500 - val[i]*ht
        rect (ulx, uly, wid, val[i]*ht)
        text (str(val[i]), ulx+5, uly-2)

    x = 100+2
    textsize(10)
    fill (255, 255, 255)
    for i in range (0,ncategories):
        cx = (wid-len(lab[i])*9)
        if cx < 0: cx = 0
        text (lab[i], x+cx/2, 520)
        x = x + wid

startdraw (600, 600)

enddraw()