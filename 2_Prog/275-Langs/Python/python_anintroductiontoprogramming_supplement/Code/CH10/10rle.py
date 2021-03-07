# Run length encoding
from struct import *
import Glib

def emit(v, n, f):
    s = pack("BB", n, v[1])
    f.write(s)

Green = (123, 210, 0)
White = (255, 255, 255)

Glib.startdraw(400, 456)
b1 = Glib.loadImage ("b1.png")
outf = open ("b1.txt", "wb")
Glib.image (b1, 0, 0)
count = 0
value = Glib.getpixel (b1,0,0)
for j in range (0, 456):
    for i in range (0, 400):
        if count ==255:              # Largest possible count.
            emit (value, count, outf)
            count = 0
        c = Glib.getpixel (b1, i, j)
        if c == value:             # Same as before
            count = count + 1
        else:
            emit(value, count, outf)
            count = 1
            value = c
if count>0:
    emit (value, count, outf)
outf.close()

Glib.enddraw()


