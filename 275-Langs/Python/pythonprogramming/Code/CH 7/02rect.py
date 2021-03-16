# Verified July 19, 2016
# All rectmodes and basic text
from Glib import *
r = 100

startdraw(400, 400)
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

fill (0)
textsize(24)
text ("Hi there", 100, 100)
enddraw()