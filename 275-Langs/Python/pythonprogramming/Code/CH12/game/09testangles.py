# Test of certain  aspects of bouncing off circles.
from Glib import *
from math import *
# Calculate the points of intersection between a line and a circle
def line_intersect_circle (l, c):
    if (l[0] == l[2]):            # Vertical
        print ("Vertical")
        m = 1000
    else:
        m = (l[1]-l[3])/(l[0]-l[2])
    b = l[1] - m*l[0]
    A = m*m + 1
    B = 2*(m*b-m*c[1]-c[0])
    C = (c[1]*c[1]) - c[2]*c[2] + c[0]*c[0] -2*b*c[1] + b*b
    disc = B*B-4*A*C
    if disc < 0.0:
        return None
    else:
        x = (-B+sqrt(disc))/(2*A)
        y = m*x+b
        if disc==0:
             return (x, y, x, y)
        x1 = (-B-sqrt(disc))/(2*A)
        y1 = m*x1+b
        return (x, y, x1, y1)


def tangent_line (xi, yi, xc, yc):
    if xi != xc:
        m = (yi-yc)/(xi-xc)
    else:
        m = 1000
    m = -(1/m)
    b = yi - m * xi
    return (m, b)

def setrange (y, low, hi):
    if y<low:
        y = low
    elif y>hi:
        y = hi
    return y

# Draw the line indicated by the given slope and intercept
def draw_line (m, b):
    y = m*10 + b
    y0 = m*300 + b
    y = setrange(y, 0, 400)
    y0 = setrange (y0,  0, 400)
    print (10, y, 300, y0)
    line (10, 500-y, 300, 500-y0)

def draw():
    global x0,y0,x1,y1,dx, m, b
    background(200)
    fill (250, 100, 200)
    ellipse (xc, yc, radius*2, radius*2)
    stroke (0)
    line (x1, 500-y1, x0, 500-y0)          # Trajectory
    l1 = (x1, y1, x0, y0)                  #  its line
    c1 = (xc, yc, radius)                  # Tile
    p1 = line_intersect_circle (l1, c1)    # Where do they meet?
    nofill()
    if p1 != None:  # They do not intersect
        d0 = (x1-p1[0])**2 + (y1-p1[1])**2  # Find nearest intersection
        d1 = (x1-p1[2])**2 + (y1-p1[3])**2
        if d0 < d1:
            xi = p1[0]
            yi = p1[1]
            ellipse (xi, 500-yi, 15, 15)      # Intersection point
        else:
            xi = p1[2]
            yi = p1[3]
            ellipse (xi, 500-yi, 15, 15)      # intersection point 2
        t = tangent_line(xi, yi, xc, yc)
        print ("Tangent: ", t)
        y3 = t[0]*(xi-100) + t[1]
        y3 = setrange (y3, -1000, 1000)
        y4 = t[0]*(xi+100) + t[1]
        y4 = setrange (y4, -1000, 1000)
        nx = xi-xc
        ny = yi-yc
        print ("(", xi, yi, ") to (", xi-100, y4, ")")
        stroke (250, 0, 0)
        line (xi, 500-yi, xi-100, 500-y3)
        line (xi, 500-yi, xi+100, 500-y4)
        angle = atan (t[0])*180./3.14159
        fill (0)
        text ("Tangent is "+str(angle), 200, 60)
        mm = (y0-y1)/(x0-x1)
        a = angle2 = atan(mm)*180/3.14159
        text ("Incoming angle is "+str(angle2), 200, 90)

        stroke (100, 200, 90)
        line (xi, 500-yi, 20*nx+xi, 500-20*ny+yi)
        normal = atan (ny/nx)*180/3.14159
        bounce = normal*2 - 180 - angle2
        text ("Bounce is "+str(bounce), 200, 400)
        x3 = 100*cos(bounce*3.1415/180)
        y3 = 100 *sin(bounce*3.1415/180)
        line (xi, 500-yi, xi+x3, 500-(yi+y3))
    x0 = x0 + dx
    if x0 > 900 or x0<0:
        dx = -dx


xc = 250
yc = 250
radius = 100
x0 = 400
y0 = 600
x1 = 0
y1 = 0
dx = 1
m = 0
b = 10
startdraw(500, 500)

enddraw()