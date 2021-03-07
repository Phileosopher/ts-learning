# Notepaper - uses lines
from Glib import *
y = 60                          # Height at which to start
startdraw(400, 600)             # Begin drawing things
background(255)                 # Paper should be white
stroke (0, 0, 200)              # Fill color = pixel color = blue
for n in range (0, 27):         # Draw 30 horizontal blue lines
    line (0, y, Width(), y)     # Draw a blue horizontal line
    y = y + 20                  # The next line is 20 pixels down
stroke (200, 0, 0)              # Pixel color red
line (25, 0, 25, Height())      # Draw a vertical red line
enddraw()
