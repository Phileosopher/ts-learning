from Glib import *

def keyPressed (k):
    global keydown
    keydown = True

def keyReleased(k):
    global keydown
    keydown = False

def draw ():
    global keydown, f
    if keydown:
        image (frames[f], 0, 0)
        f = f + 1
        if (f > 10):
            f = 1

startdraw(320, 240)
keydown = False
frames = []
for i in range (1, 10):
    s = "images/a00"+str(i) +".bmp"
    x = loadImage (s)
    frames = frames + [x,]
x = loadImage ("images/a010.bmp")
frames = frames + [x,]
x = loadImage ("images/a011.bmp")
frames = frames + [x,]
f = 1
image (frames[0], 0, 0)
enddraw()