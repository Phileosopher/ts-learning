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
        self.speed = 5
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
        self.sounds = impacts()    # Create a sound effect class instance

    def hitspaddle (self):
        if self.y<=paddleY and self.y+self.dy>=paddleY:
            if p.inpaddle(self.x):
                return True
        return False

    def distance (self, x, y):
        return (  (x-self.x)*(x-self.x) + (y-self.y)*(y-self.y)  )

    def hitsTile(self):
        global hit
        for k in tiles:
            if k.active:
                if self.distance (k.x, k.y) <= k.size*k.size:
                    if k:
                        self.sounds.playBallTile ()
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
            self.sounds.playBallPaddle()
            self.dy = -self.dy
            self.dx = -5 + (1./9.)*(self.x-p.x)
        t = self.hitsTile()
        if t != None:
            t.deactivate()
            score = score + t.points
            self.dy = -self.dy
        if (self.x <= self.size/2) or  (self.x >= Glib.width-self.size/4):
            self.sounds.playBallWall()
            self.dx = -self.dx
        if self.y <= self.size/2:
            self.sounds.playBallWall()
            self.dy = -self.dy
        if self.y >= Glib.height:
            self.sounds.playBallGone()
            self.active = False

class impacts():
    def __init__(self):
        self.ballTile = Glib.loadSound ("ballTile.wav")
        self.ballPaddle = Glib.loadSound("ballPaddle.wav")
        self.ballWall = Glib.loadSound("ballWall.wav")
        self.ballGone = Glib.loadSound("ballGone.wav")

    def playBallTile(self):
        Glib.playSound(self.ballTile)
    def playBallPaddle(self):
        Glib.playSound(self.ballPaddle)
    def playBallWall(self):
        Glib.playSound(self.ballWall)
    def playBallGone(self):
        Glib.playSound(self.ballGone)

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