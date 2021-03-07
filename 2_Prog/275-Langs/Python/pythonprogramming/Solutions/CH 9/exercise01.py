# exercise 9.01
import Glib
from math import *

def draw ():
    global oldx, oldy
    Glib.background (230, 230, 0)
    dx = Glib.mouseX - oldx
    dy = Glib.mouseY - oldy
    v = sqrt (dx*dx + dy*dy)
    s = "Mouse speed is "+str(v)
    oldx = Glib.mouseX
    oldy = Glib.mouseY
    Glib.text (s, 10, 50)

Glib.startdraw(500, 500)
oldx = 0
oldy = 0
Glib.enddraw()

