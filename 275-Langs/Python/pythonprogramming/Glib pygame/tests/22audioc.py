from Glib import *
from wave import *
import struct

def draw ():
    global frame, v
    setVideoFrame(v, frame)
    frame = frame + 1
    print (getVideoPixel (v, 100, 100))
    ellipse (100, 100, 10, 10)

startdraw(400,400)
v = loadVideo ("carclub2.mpg")
frame = 1

nofill()
#capture("out.jpg")
enddraw()