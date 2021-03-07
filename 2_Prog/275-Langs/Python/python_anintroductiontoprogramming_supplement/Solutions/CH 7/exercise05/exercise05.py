# Exercise 5 - polygons and text
from Glib import *
from math import *

cvt = 3.14159/180.0

def pent (x, y, r):
    x0 = x+r
    y0 = y
    for i in range (0, 6):
        x1 = x+r*cos(i*72.0*cvt)
        y1 = y-r*sin(i*72.0*cvt)
        line (x0, y0, x1, y1)
        x0 = x1
        y0 = y1

def hex(x, y, r):
    x0 = x+r
    y0 = y
    for i in range (0, 7):
        x1 = x+r*cos(i*60.0*cvt)
        y1 = y-r*sin(i*60.0*cvt)
        line (x0, y0, x1, y1)
        x0 = x1
        y0 = y1

startdraw(400, 400)
fill (0)
nofill()
background (255)
triangle (100, 100, 50, 150, 150, 150)
text ("Triangle", 70, 90)
rect (200, 100, 75, 75)
text ("Square", 210, 90)
pent(100, 300, 60)
text ("Pentagon", 75, 230)
hex (250, 300, 60)
text ("Hexagon", 230, 230)
enddraw()