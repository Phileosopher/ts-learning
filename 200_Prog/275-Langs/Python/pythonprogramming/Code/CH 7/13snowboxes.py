# Snow boxes
# Original by Noah Larsen, @earlatron in Processing
from Glib import *
from random import *

startdraw (640, 480)
background(randrange(0,75), randrange(150,255), randrange(0,75))

fill (255, 255, 255)
for i in range(0,10000):
    point (randrange(0,Width()), randrange(0,Height()))
for i in range(0,20):
    xs = randrange (0, Width())
    ys = randrange (0, Height())
    xe = randrange (xs, xs+randrange(30, 300))
    ye = randrange (ys, ys+randrange(30, 300))
    for j in range(0,10000):
        point (randrange(xs, xe+1),randrange(ys, ye+1))
enddraw()