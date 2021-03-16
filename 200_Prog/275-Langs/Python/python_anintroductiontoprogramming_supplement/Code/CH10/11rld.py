# Run length encoding
from struct import *
import Glib

Glib.startdraw(400, 456)
inf = open ("b1.txt", "rb")
i = 0
j = 0
cols = 400
rows = 456
while True:
    s = inf.read(2)
    if len(s) <= 0:
        break

    c,v = unpack("BB", s)
    print (c, v)
    if v == 255:
        Glib.fill (255, 255, 255)
    else:
        Glib.fill (123, 210, 0)

    for k in range (0, c):
        if i >= cols:
            i = 0
            j = j + 1
        Glib.point (i, j)
        i = i + 1
    if j>= 456:
        break
Glib.enddraw()


