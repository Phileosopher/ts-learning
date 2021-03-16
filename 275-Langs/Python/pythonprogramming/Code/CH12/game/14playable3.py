# All three classes together
# Third playable breakout style game
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
            Glib.ellipse (self.x, self.y, self.size, self.size)    # Draw circle

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
        self.color = (230, 0, 230)    # Ball color. A purple
        self.size = 9                 # Ball diameter

    # Returns True if the ball hits the paddle
    def hitspaddle (self):
        if self.y<=paddleY and self.y+self.dy>=paddleY: # Above now and below next
            if p.inpaddle(self.x):                      # And in the paddle x range
                return True
        return False

    # Basic Euclidean distance, but squared
    def distance (self, x, y):
        return (  (x-self.x)*(x-self.x) + (y-self.y)*(y-self.y)  )

    # Returns the tile that the ball will hit, if any
    def hitsTile(self):
        for k in tiles:   # For all active tiles
            if k.active:  # if the distance between the ball and tile is small enough
                if self.distance (k.x, k.y) <= k.size*k.size/2:  # Then they collide
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

    # Draw the ball in its current position. Check for collisions with
    # the sides, the paddle, and any tile. Check for game over.
    def draw(self):
        global score, state, pausestate
        global balls_remaining, gameoverstate

        Glib.fill (self.color[0], self.color[1], self.color[2])  # Ball color
        Glib.ellipse (self.x, self.y, self.size, self.size)      # Ball is a circle
        self.x = self.x + self.dx            # Change position for next frame
        self.y = self.y + self.dy
        if self.hitspaddle():                   # Does the ball strike the paddle?
            self.dy = -self.dy                  # Yes. Reverse Y direction
            self.dx = -5 + (1./9.)*(self.x-p.x) # and set dx according to strike point
        t = self.hitsTile()                     # Does the ball hit a tile?
        if t != None:
            t.deactivate()                      # Yes. Deactivate the tile
            score = score + t.points            # Score some points
            self.bounce (t)                          # This is a simple bounce
        if (self.x <= self.size/2) or  (self.x >= Glib.width-self.size/4):
            self.dx = -self.dx                  # Bounce from a wall
        if self.y <= self.size/2:
            self.dy = -self.dy                  # Bounce from the roof
        if self.y >= Glib.height:               # LEaves the play area?
            if balls_remaining>0:               # Yes. Balls left?
                state = pausestate              # Yes. Pause
                balls_remaining = balls_remaining-1 # One less ball ...
            else:
                state = gameoverstate           # No. Game over

# This implements the play state. The ball is in play.
def state0():
    global tiles,p,f,b,movingleft,movingright
    global score
    Glib.background(200)        # Redraw.
# Tiles
    for k in tiles:             # Draw all active tiles
        k.draw()
# Paddle
    if movingleft:              # If the paddle is in motion, move it
        p.moveleft()
    elif movingright:
        p.moveright()
    p.draw()                    # Draw the paddle
# Ball
    b.draw()                    # Draw the ball
    Glib.text ("Score: "+str(score), 10, 30)   # Draw score and remaining balls
    Glib.text ("Balls remaining:"+str(balls_remaining), 220, 30)

# This is the pause state. A keypress will return to play state.
def state1():
    global tiles,p,f,b,movingleft,movingright
    global score, maxscore
    Glib.background(200)        # Redraw
    for k in tiles:             # Draw all active tiles
        k.draw()
    p.draw()                    # Draw paddle but do not move it
    Glib.text ("Score: "+str(score), 10, 30)   # SCore and remaining balls
    Glib.text ("Balls remaining:"+str(balls_remaining), 220, 30)

# Draw the game. Draw all components, depemnding on the current state
def draw ():
    global state, playstate, pausestate, score, gameoverstate
    if state == playstate:     # Playing.
        state0()
        if score >= 540:
            state = gameoverstate
    elif state == pausestate: # Pausing
        state1()
    else:
        if score >= maxscore:          # The gameover state. Win?
            Glib.background (0,230, 0) # Yes
            Glib.text ("You Win", 200, 200)
        else:
            Glib.background (100, 10, 10); # Lose, there are btiles left.
            Glib.text ("You Lose", 200, 200)
            Glib.text ("Score: "+str(score), 10, 30)

# This function is called in the pause state to resume the game
# The ball is placed on the play area and state becomes play.
def resume():
    global state, playstate
    b.x = randrange (30, Glib.width-30)    # Random x location
    b.y = 250
    state = playstate

# When the  arrow keys are pressed in the play state the paddle moves.
# When any key is pressed in the pause state resume is called to start the game.
def keyPressed (k):
    global movingleft, movingright, state, pausestate
    if state == pausestate:
        resume()
    if k == Glib.K_LEFT:
        movingleft = True
    elif k == Glib.K_RIGHT:
        movingright = True

# Keyreleased. This resets the moving flags so that the paddle motion stops
def keyReleased (k):
    global movingleft, movingright
    if k == Glib.K_LEFT:
        movingleft = False
    elif k == Glib.K_RIGHT:
        movingright = False

movingleft = False       # Should the paddle more left?
movingright = False      # Should the paddle move right?
paddleY = 320
score = 0
Glib.startdraw(360, 350)
red = (250, 0, 0)
tiles = ()
playstate = 0
pausestate = 1
gameoverstate = 2
state = playstate
balls_remaining = 2
maxscore = 540

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