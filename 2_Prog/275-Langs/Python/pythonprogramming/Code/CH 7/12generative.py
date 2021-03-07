from Glib import *
from math import *
from random import *

conv = 3.1415/180.0
startdraw(800,600)
background(9)
r = 255
for i in range (0, 180, 2):
    stroke (r, 128, 128)
    line (400, 600, cos(i*conv)*500, sin(i*conv)*500)
    r = r - 0.5

x = randrange(100, Width())
y = randrange (100, Height()-100)
r = 255
for i in range (1, 180, 2):
    stroke (128, r, 128)
    line (x, y, sin(i*conv)*500, cos(i*conv)*500)
    r = r - 0.5

x = randrange(100, Width())
y = randrange (100, Height()-100)
r = 255
for i in range (1, 180, 2):
    stroke (r, 200, r)
    line (x, y, sin(-i*conv)*500, cos(i*conv)*500)
    r = r - 0.5

enddraw()
