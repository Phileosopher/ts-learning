from Glib import *
import Glib
from random import *

x0 = 100            # upper left button position
y0 = 100
w = 60              # Button size
h = 20
bc = cvtColor(200)  # Initial color
active = False      # Is the button currently active?

def draw ():
    global bc, w, h, x0, x1, y0,y1, active
    background (red(bc), green(bc), blue(bc))   # Set background color to bc
    x = Glib.mouseX                             # Is the mouse in the rectangle?
    y = Glib.mouseY
    if x>x0 and x<x0+w and y>y0 and y<y0+h:
        fill (50, 200, 50)                      # YES. Button is active. Green
        active = True
    else:
        fill (200, 50, 50)                      # NO. Button is inactive. Red
        active = False
    rect (x0, y0, w, h)                         # Draw the button

def mouseReleased (b):
    global active, bc
    if active and b==0:      # Button active? Left button released?
                             # If so generate a random background color.
        bc = (randrange (100, 200), randrange(100,200), randrange(100, 200))

startdraw(400, 400)
enddraw()
