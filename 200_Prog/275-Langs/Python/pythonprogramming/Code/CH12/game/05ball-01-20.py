# Tile class development step 0
import Glib
from random import *

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
    global b
    Glib.background(200)
    b.draw()


Glib.startdraw(360, 350)
b = ball (300, 300)
Glib.enddraw()