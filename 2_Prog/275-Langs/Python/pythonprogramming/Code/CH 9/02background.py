from Glib import *
import Glib

def draw ():
    r = int((Glib.mouseX/width) *255.0)
    g = int((Glib.mouseY/height)*255.0)
    background (r, g, 128)

startdraw(400, 400)
enddraw()
