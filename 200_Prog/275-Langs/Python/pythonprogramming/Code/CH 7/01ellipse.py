# Verified July 19, 2016
# All ellipsemodes, color fill, grey background, window size

from Glib import *

startdraw(400, 400)
background(200)
fill (200, 200, 0)
ellipsemode (CENTER)
ellipse (100, 100, 30, 40);
ellipsemode (RADIUS)
ellipse (200, 100, 30, 40);
ellipsemode(CORNER)
ellipse (100, 200, 30, 40);
ellipsemode(CORNERS)
ellipse (200, 200, 230, 240);
enddraw()