# Test 07 viper histogram verified 2015-11-26
from Glib import *

title = "Users of ViPER Android Game"
ncategories = 8
maxsize = 1000
hlabel = "Age of Visitor"
vlabel = "Number of Visitors"
val = (120, 834, 700, 413, 400, 211, 90, 25)
lab = ("0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35+")

def draw ():
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
        rect (ulx, uly, wid, val[i]*ht-2)
        text (str(val[i]), ulx+5, uly-2)

    x = 100+2
    textsize(10)
    fill (255, 255, 255)
    for i in range (0,ncategories):
        cx = (wid-len(lab[i])*9)
        if cx < 0: cx = 0
        text (lab[i], x+cx, 520)
        x = x + wid

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

startdraw (600, 600)
background(180)
setfont("Helvetica")
strokeweight (3)

enddraw()
