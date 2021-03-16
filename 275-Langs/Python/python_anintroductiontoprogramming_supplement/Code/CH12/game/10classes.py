# All three classes together
import Glib
from random import *
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


class tile():
    def __init__(self, x, y, color, points):
        self.x = x
        self.y = y
        self.color = color
        self.points = points
        self.active = True
        self.size = 30

    def draw(self):
        if self.active:
            Glib.fill (self.color[0], self.color[1], self.color[2])
            Glib.ellipse (self.x, self.y, self.size, self.size)

    def deactivate (self):
        self.active = False

class paddle():
    def __init__(self, x):
        self.x = x
        self.y = paddleY
        self.speed = 6
        self.color = (0,0,0)
        self.width = 90
        self.height = 12

    def draw(self):
        Glib.fill (self.color[0], self.color[1], self.color[2])
        Glib.rect (self.x, self.y, self.width, self.height)

    def moveleft(self):
        if self.x <= self.speed:
           self.x = 0
        else:
            self.x = self.x - self.speed

    def moveright (self):
        if self.x > Glib.Width()-self.width-self.speed:
           self.x = Glib.Width()-self.width
        else:
            self.x = self.x + self.speed

    def inpaddle(self, x):
        if x < self.x:
            return False
        if x > self.x + self.width:
            return False
        return True

class ball():
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.dx = 3
        self.dy = -4
        self.active = True
        self.color = (230, 0, 230)
        self.size = 9

    def hitspaddle (self):
        if self.y<=paddleY and self.y+self.dy>=paddleY:
            if p.inpaddle(self.x):
                return True
        return False

    def distance (self, x, y):
        return (  sqrt((x-self.x)**2 + (y-self.y)**2)  )

    def hitsTile(self):
        for k in tiles:
            if k.active:
                if self.distance (k.x, k.y) <= k.size:
                    return k
        return None

    def bounce (self, t):
        l1 = (self.x, self.y, self.x+self.dx, self.y+self.dy)
        c1 = (t.x, t.y, t.size)
        p1 = line_intersect_circle (l1, c1)
        if p1 is None:
            return (self.dx, self.dy)
        d0 = (self.x-p1[0])**2 + (self.y-p1[1])**2  # Find nearest intersection
        d1 = (self.y-p1[2])**2 + (self.y-p1[3])**2
        if d0 < d1:
            xi = p1[0]
            yi = p1[1]
        else:
            xi = p1[2]
            yi = p1[3]
        tangent = tangent_line (xi, yi, t.x, t.y)
        nx = xi-t.x
        if nx == 0:
            nx = 1000
        ny = yi-t.y
        tangent_angle = atan (tangent[0])*180.0/3.14159
        incoming = atan(self.dy/self.dx)*180.0/3.14159
        normal_angle = atan(ny/nx)*180/3.14159
        bounce_angle = normal_angle*2 - 180 - incoming
        dx = cos(bounce_angle)*7
        dy = sin(bounce_angle)*7
        print ("Incoming ", incoming,
               " tangent: ", tangent_angle,
               "normal:", normal_angle,
               "Bounce:", bounce_angle)
        return (dx, dy)

    def move (self):
        global score
        self.x = self.x + self.dx
        self.y = self.y + self.dy

        if self.hitspaddle():
            self.dy = -self.dy

        t = self.hitsTile()
        if t != None:
            t.deactivate()
            score = score + t.points
            self.dx, self.dy = self.bounce (t)
        if (self.x <= self.size/2) or  (self.x >= Glib.width-self.size/4):
            self.dx = -self.dx
        if self.y <= self.size/2:
            self.dy = -self.dy
        elif self.dy >= Glib.height:
            self.active = False

    def draw(self):
        global score
        if not self.active:
            return
        self.move()
        Glib.fill (self.color[0], self.color[1], self.color[2])
        Glib.ellipse (self.x, self.y, self.size, self.size)
        Glib.text ("Score: "+str(score), 10, 30)

def draw():
    global tiles,p,f,b,movingleft,movingright
    Glib.background(200)
# Tiles
    for k in tiles:
        k.draw()
# Paddle
    if movingleft:
        p.moveleft()
    elif movingright:
        p.moveright()
    p.draw()
# Ball
    b.draw()

def keyPressed (k):
    global movingleft, movingright
    if k == Glib.K_LEFT:
        movingleft = True
    elif k == Glib.K_RIGHT:
        movingright = True

def keyReleased (k):
    global movingleft, movingright
    if k == Glib.K_LEFT:
        movingleft = False
    elif k == Glib.K_RIGHT:
        movingright = False

movingleft = False
movingright = False
paddleY = 320
score = 0
Glib.startdraw(360, 350)
red = (250, 0, 0)
tiles = ()
for i in range (0, 12):
    tiles = tiles + (tile(i*30+15, 90, red, 15),)
f = True
p = paddle (130)
b = ball (300, 300)
Glib.enddraw()