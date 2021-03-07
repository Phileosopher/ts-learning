# Exercise 3 - Pyramid
from Glib import *

def brick (x, y):
    rect (x, y, brickwidth, brickheight)

def bricks (x, y, n):
    xx = x
    for i in range (0, n):
        brick (xx, y)
        xx = xx + brickwidth


brickwidth = 15
brickheight = 6
startdraw(400, 150)
background (255)
fill (120)
x = 100
y = 130
for i in range (0, 15):
    bricks(x, y, 15-i)
    x = x + brickwidth/2
    y = y - brickheight
enddraw()