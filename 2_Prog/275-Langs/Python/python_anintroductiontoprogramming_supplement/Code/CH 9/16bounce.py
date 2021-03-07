# Bouncing ball animation.
from Glib import *

def draw ():
    global dx, dy, x, y
    background (200)          # Erase the prior frame
    x = x + dx                # Change ball position
    y = y + dy
    if x<=15 or x>=width-15:  # Bounce in X direction?
        playSound (s)
        dx = -dx
    if y<=15 or y>=height-15: # Bounce in Y direction?
        dy = -dy
        playSound(s)
    ellipse (x, y, 30, 30)    # Draw the ball

startdraw(200, 200)
x = 100                       # Initial x position of the ball
y = 100                       # Initial y position
dx = 3                        # Speed in x
dy = 2                        # Speed in y
s = loadSound ("bounce.wav")
fill (30, 200, 20)            # Fill with green
enddraw()
