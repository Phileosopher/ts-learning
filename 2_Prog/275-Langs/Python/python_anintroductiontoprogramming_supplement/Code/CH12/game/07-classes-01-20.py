# All three classes together
import Glib
from random import *

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

class paddle():
    def __init__(self, x):
        self.x = x
        self.y = 320
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

class ball():
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.dx = 3
        self.dy = -4
        self.active = True
        self.color = (230, 0, 230)
        self.size = 9

    def draw(self):
        if not self.active:
            return
        Glib.fill (self.color[0], self.color[1], self.color[2])
        Glib.ellipse (self.x, self.y, self.size, self.size)
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        if (self.x <= self.size/2) or \
              (self.x >= Glib.width-self.size/4):
            self.dx = -self.dx
        if self.y <= self.size/2:
            self.dy = -self.dy
        elif self.dy >= Glib.height:
            self.active = False

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
Glib.startdraw(360, 350)
red = (250, 0, 0)
tiles = ()
for i in range (0, 12):
    tiles = tiles + (tile(i*30+15, 90, red, 15),)
f = True
p = paddle (130)
b = ball (300, 300)
Glib.enddraw()