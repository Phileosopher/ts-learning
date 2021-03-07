# Tile class development step 0
import Glib
from random import *

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

def draw():
    global p,f
    Glib.background(200)
    p.draw()
    if f:
        p.moveright()
    else:
        p.moveleft()
    if random()< .01:
        f = not f

Glib.startdraw(360, 350)
f = True
p = paddle (130)
Glib.enddraw()