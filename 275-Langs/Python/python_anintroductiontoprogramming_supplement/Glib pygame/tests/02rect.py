# Verified Nov 26 2015
# All rectmodes, mouse coordinates and mouseup, animated color, basic text
from Glib import *
r = 100
x1= x2 = y1 = y2 = -1

def initialize():
    print("Initializing")
    x1 = x2 = -1

def draw ():
    global r, x1,x2, y1,y2
    background(200)
    fill (r, 200, 200)
    rectmode(CENTER)
    rect (100, 100, 30, 40);
    rectmode (RADIUS)
    rect (200, 100, 30, 40);
    rectmode(CORNER)
    rect (100, 200, 30, 40);
    rectmode(CORNERS)
    rect (200, 200, 230, 240);
    r = r + 1
    if r > 255: r = 100
    if x2 > 0: line (x1,y1, x2,y2)
    fill (0)
    textsize(24)
    text ("Hi there", 100, 100)

def mouseReleased(b):
    global x1,y1,x2,y2
    m = mouse()
    if x1 < 0:
        x1 = m[0]
        y1 = m[1]
    elif x2 < 0:
        x2 = m[0]
        y2 = m[1]
    else:
        x1 = x2 = -1

startdraw(400, 400)

enddraw()