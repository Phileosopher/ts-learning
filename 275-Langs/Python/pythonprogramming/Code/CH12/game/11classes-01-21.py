# All three classes together
import Glib
from random import *
from math import *

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
        self.speed = 3
        self.color = (0,0,0)
        self.width = 90
        self.height = 10

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

    def draw(self):
        global score
        if not self.active:
            return
        Glib.fill (self.color[0], self.color[1], self.color[2])
        Glib.ellipse (self.x, self.y, self.size, self.size)
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        if self.hitspaddle():
            self.dy = -self.dy
        t = self.hitsTile()
        if t != None:
            t.deactivate()
            score = score + t.points
            self.dy = -self.dy
        if (self.x <= self.size/2) or  (self.x >= Glib.width-self.size/4):
            self.dx = -self.dx
        if self.y <= self.size/2:
            self.dy = -self.dy
        elif self.dy >= Glib.height:
            self.active = False
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