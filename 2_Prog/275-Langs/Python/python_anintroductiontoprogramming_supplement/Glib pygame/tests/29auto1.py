from Glib import *
from random import *

def draw():
    global f,q
    for i in q:
        i.draw()


startdraw(500, 500)
s = Gvideo ("oceanquest.mpg")
s.locVideo (20, 20, 150, 150)

q = (s, s.copy(175, 20, 150, 150), s.copy (20, 175, 150, 150),
     s.copy(175, 175, 150, 150))
for i in  q:
    i.play()
enddraw()