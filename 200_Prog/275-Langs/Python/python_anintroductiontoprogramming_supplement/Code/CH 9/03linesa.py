from Glib import *
import Glib
x0 = x1 = y1 = y0 = 0

def draw ():
    global d, x0, y0
    background(200, 200, 0)
    if d:
        line (x0, y0, Glib.mouseX, Glib.mouseY)

def mousePressed (b):
    global x0, y0, d
    x0 = Glib.mouseX
    y0 = Glib.mouseY
    d = True

def mouseReleased (b):
    global x0, y0, x1, y1, d
    x1 = Glib.mouseX
    y1 = Glib.mouseY
    line (x0, y0, x1,y1)
    d = False

startdraw(400, 400)
d = False
enddraw()
