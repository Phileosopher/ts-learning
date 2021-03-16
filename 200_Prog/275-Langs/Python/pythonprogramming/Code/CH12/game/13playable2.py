# Second playable breakout style game
import Glib
from random import *
from math import *

# The tile class represents the targets. When struck by the ball,
# points are scored and the tile vanishes. It is circular.
class tile():
    def __init__(self, x, y, color, points):
        self.x = x             # X coordinate of the tile center
        self.y = y             # Y coordinate of thetile center
        self.color = color     # The color of this tile
        self.points = points   # Number of points it is worth
        self.active = True     # Is it visible?
        self.size = 30         # Circle diameter

    # Draw this tile
    def draw(self):
        if self.active:       # Don't draw it if it is not active
            Glib.fill (self.color[0], self.color[1], self.color[2]) # Set color
            Glib.ellipse (self.x, self.y, self.size, self.size)     # Draw circle

    # Make this tile inactive. It happens when hit by the ball.
    def deactivate (self):
        self.active = False

# The paddle class represents the moveable paddle at the bottom of the scree3n.
# It is controlled by the user, and is rectangular in shape.
class paddle():
    def __init__(self, x):
        self.x = x               # X location of the left side of the paddle
        self.y = paddleY         # Y coordinate of the upper surface
        self.speed = 5           # Pixels per frame motion, when moving
        self.color = (0,0,0)     # Color - this one is black
        self.width = 90          # Paddle width, in pixels
        self.height = 10         # Paddle thickness

    # Draw the paddle in its current position
    def draw(self):
        Glib.fill (self.color[0], self.color[1], self.color[2])  # Color
        Glib.rect (self.x, self.y, self.width, self.height)      # Rectangle

    # Move the paddle left at standard speed. This means the left key is down
    def moveleft(self):
        if self.x <= self.speed:           # Do not go past the left edge
           self.x = 0
        else:
            self.x = self.x - self.speed   # Change X value negatively.

    # Move the paddle right at standard speed. This means the right key is down
    def moveright (self):
        if self.x > Glib.Width()-self.width-self.speed:  # Don't pass the right edge
           self.x = Glib.Width()-self.width
        else:
            self.x = self.x + self.speed                 # Change X positively

    # Is the specified X value between the left and right edges of the paddle?
    def inpaddle(self, x):
        if x < self.x:
            return False
        if x > self.x + self.width:
            return False
        return True

# The ball class represents the bouncing ball in the game. It bounces off of
# the top and sides of the play area, off of tiles, and off of the paddle.
class ball():
    def __init__ (self, x, y):
        self.x = x                    # Current X location of ball center
        self.y = y                    # Current Y location of ball center
        self.dx = 3                   # Current X speed, pixels per frame
        self.dy = -4                  # Current Y speed
        self.active = True
        self.color = (230, 0, 230)
        self.size = 9

    def hitspaddle (self):
        if self.y<=paddleY and self.y+self.dy>=paddleY:
            if p.inpaddle(self.x):
                return True
        return False

    def distance (self, x, y):
        return (  (x-self.x)*(x-self.x) + (y-self.y)*(y-self.y)  )

    def hitsTile(self):
        for k in tiles:
            dd = (k.size/2 + self.size/2)
            dd = dd * dd
            if k.active:
                if self.distance (k.x, k.y) <= dd:
                    return k
        return None

    def distance2 (self, x0,y0, x1, y1):
        return (x0-x1)*(x0-x1) + (y0-y1)*(y0-y1)

    def bounce (self, t):
        dd = t.size/2 + self.size/2
        dd = dd * dd
        collide = False
        if self.distance2 (self.x, self.y, t.x, t.y) >= dd and \
        self.distance2 (self.x+self.dx, self.y+self.dy, t.x, t.y) < dd:
            self.x = self.x + self.dx/2
            self.y = self.y + self.dy/2
            collide = True
        elif self.distance2 (self.x, self.y, t.x, t.y) < dd:
            collide = True
        else:
            self.x = self.x + self.dx
            self.y = self.y + self.dy
        if not collide:
            return
        while self.distance2 (self.x, self.y, t.x, t.y) < dd:
            self.x = self.x - self.dx*0.5
            self.y = self.y - self.dy*0.5
        if self.x != t.x:
            a = atan ((self.y-t.x)/(self.x-t.y))
            a = a * 180./3.1415
        else:
            a = 90.0
        if a >= -45.0 and a<=45.0:
            self.dx = -self.dx
        else:
            self.dy = -self.dy

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
            self.dx = -5 + (1./9.)*(self.x-p.x)
        t = self.hitsTile()
        if t != None:
            t.deactivate()
            score = score + t.points
#            self.dy = -self.dy
            self.bounce (t)
        if (self.x <= self.size/2) or  (self.x >= Glib.width-self.size/4):
            self.dx = -self.dx
        if self.y <= self.size/2:
            self.dy = -self.dy
        elif self.dy >= Glib.height:
            self.active = False

def draw():
    global tiles,p,f,b,movingleft,movingright
    global score
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
    Glib.text ("Score: "+str(score), 10, 30)

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

for i in range (0, 12):         # Draw top row of tiles
    tiles = tiles + (tile(i*30+15, 60, (100,100,240), 5),)
for i in range (0, 12):         # Draw 2nd row of tiles
    tiles = tiles + (tile(i*30+15, 90, (220,220,90), 10),)
for i in range (0, 12):         # Draw 3rd row of tiles
    tiles = tiles + (tile(i*30+15, 120, red, 15),)
for i in range (0, 12):         # Draw 4th row of tiles
    tiles = tiles + (tile(i*30+15, 150, (180,150,30), 10),)
for i in range (0, 12):         # Draw top row of tiles
    tiles = tiles + (tile(i*30+15, 180, (90,220,80), 5),)
f = True
p = paddle (130)
b = ball (300, 300)
Glib.enddraw()