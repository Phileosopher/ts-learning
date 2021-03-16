# Exercise 1 - Circles filled with color
from Glib import *

startdraw(500, 450)
background (255)
fill (255, 0, 0)            # Red
ellipse (250, 60, 40, 40)
fill (0, 255, 0)            # Green
ellipse (125, 250, 40, 40)
fill (0, 0, 255)            # Blue
ellipse (390, 250, 40, 40)

fill (255, 255, 0)          # Yellow
ellipse (150, 135, 40, 40)
fill (255, 0, 255)          # Magenta
ellipse (350, 135, 40, 40)
fill (0, 255, 255)          # Cyan
ellipse (250, 350, 40, 40)
enddraw()