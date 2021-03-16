# Test of approximate bounces
from Glib import *
from math import *

def mousePressed (k):
    global ballx, bally, x2, y2, dx, dy
    if x2 > 0:
        ballx = bally = -1
    if ballx > 0:
        x2 = mouseX()
        y2 = mouseY()
        dx = (x2-ballx)/30
        dy = (y2-bally)/30
    else:
        text ("Place first", 10, 20)
        ballx= mouseX()
        bally = mouseY()
        x2 = y2 = -1
        dx = dy = 0.01

def distance2 (x0,y0, x1, y1):
    return (x0-x1)*(x0-x1) + (y0-y1)*(y0-y1)

def draw ():
    global ballx, bally, dx, dy
    collide = False
    background (80, 200, 60)
    ellipse (100, 100, 30, 30)
    ellipse (ballx, bally, 8, 8)
    ballx = ballx + dx
    bally = bally + dy
    print ("Draw")
    if distance2 (ballx, bally, 100, 100) >= 19*19 and \
       distance2 (ballx+dx, bally+dy, 100, 100) < 19*19:
        ballx = ballx + dx/2
        bally = bally + dy/2
        collide = True
    elif distance2 (ballx, bally, 100, 100) < 19*19:
        collide = True
    else:
        ballx = ballx + dx
        bally = bally + dy
    if not collide:
        return
    while distance2 (ballx, bally, 100, 100) < 19*19:
        ballx = ballx - dx*0.5
        bally = bally - dy*0.5
        print ("Backing out", ballx, bally, dx, dy)
    if ballx != 100:
        a = atan ((bally-100)/(ballx-100))
        a = a * 180./3.1415
    else:
        a = 90.0
    if a >= -45.0 and a<=45.0:
        dx = -dx
    else:
        dy = -dy

ballx = 300
bally = 300
dx = 0
dy = 0
x0 = 0
y0 = 0
x2 = 0
y2 = 0

startdraw(400, 400)
ellipse (100, 100, 30, 30)
enddraw()