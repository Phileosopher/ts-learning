from Glib import *
from random import *

def draw ():
    global dx, dy, x, y
    background (200)          # Erase the prior frame
    for i in range(0,n):
        x[i] = x[i] + dx[i]                # Change ball position
        y[i] = y[i] + dy[i]
        if x[i]<=sizes[i]/2 or x[i]>=width-sizes[i]/2:  # Bounce in X direction?
            dx[i] = -dx[i]
        if y[i]<=sizes[i]/2 or y[i]>=height-sizes[i]/2: # Bounce in Y direction?
            dy[i] = -dy[i]
        fill (red(colors[i]), green(colors[i]), blue(colors[i]))
        ellipse (x[i], y[i], sizes[i], sizes[i])    # Draw the ball

startdraw(400, 400)
n = 50
x = []                        # Initial x position of the balls
y = []                        # Initial y position
dx = []                       # Speed in x
dy = []                       # Speed in y
colors = []
sizes = []
for i in range (0,n):
    x = x + [randrange(15,width-15)]
    y = y + [randrange(15,height-15)]
    dx = dx + [randrange (-2, 2)]
    dy = dy + [randrange (-2, 2)]
    sizes = sizes + [randrange (2,30)]
    colors = colors +[(randrange(100, 200),randrange(100, 200),randrange(100, 200)),]
nostroke()
enddraw()