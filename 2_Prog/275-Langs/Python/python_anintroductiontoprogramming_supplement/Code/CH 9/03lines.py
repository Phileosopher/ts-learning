from Glib import *
import Glib
x0 = x1 = y1 = y0 = 0

def mousePressed (b):
    global x0, y0
    x0 = Glib.mouseX
    y0 = Glib.mouseY

def mouseReleased (b):
    global x1, y1
    x1 = Glib.mouseX
    y1 = Glib.mouseY
    line (x0, y0, x1,y1)

startdraw(400, 400)
enddraw()
