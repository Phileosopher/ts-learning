from Glib import *
from random import *

class Ball:
    def __init__ (self):
        self.x = randrange (15, width-15)
        self.y = randrange (15, height-15)
        self.dx = randrange (-2, 2)
        self.dy = randrange (-2, 2)
        self.size = randrange (2, 30)
        self.color = (randrange (100, 200), randrange (100, 200),randrange (100, 200))

    def draw (self):
        self.x = self.x + self.dx                # Change ball position
        self.y = self.y + self.dy
        if self.x<=self.size/2 or self.x>=width-self.size/2:  # Bounce in X direction?
            self.dx = -self.dx
        if self.y<=self.size/2 or self.y>=height-self.size/2: # Bounce in Y direction?
            self.dy = -self.dy
        fill(self.color[0], self.color[1], self.color[2], self.color[3])
        ellipse (self.x, self.y, self.size, self.size)    # Draw the ball

def draw ():
    global dx, dy, x, y
    background (200)          # Erase the prior frame
    for i in range(0,n):
        balls[i].draw()

startdraw(400, 400)
n = 50
balls = []
for i in range (0,n):
    balls = balls + [Ball()]
nostroke()
enddraw()