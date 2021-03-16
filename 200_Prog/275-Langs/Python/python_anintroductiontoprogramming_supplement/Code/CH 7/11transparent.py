# Test 11 - Transparency 2016-07-19
from Glib import *

s = imageSize("../07images/car.gif")    # Get size of image
startdraw(s[0], s[1])           # Open window of the right size
s  = loadImage("../07images/perseus.gif")   # Background image
t = loadImage ("../07images/car.gif")       # Car image with transparency
image (s, 0, 0)                 # Display background first
image (t, 0, 0)                 # then display the car image
enddraw()
