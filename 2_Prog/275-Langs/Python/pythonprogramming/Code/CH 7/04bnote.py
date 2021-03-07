# Test 6 - Notepaper verified 2015-11-26
# point
from Glib import *
y = 60                            #  Height at which to start

startdraw(400, 600)	          # Begin drawing things
background(255)
y = 60
fill (0, 0, 200)              # Fill color = pixel color = blue
for n in range (0, 27):       # Draw 30 horizontal blue lines
    for x in range (0,Width()): # Draw all pixels in one line
        point (x, y)          # Draw a blue pixel
    y = y + 20                # The next line is 20 pixels down
fill (200, 0, 0)              # Pixel color red
for y in range (0, Height()):   # Draw connected vertical pixels
    point (25, y)             #  to form the margin line
enddraw()
