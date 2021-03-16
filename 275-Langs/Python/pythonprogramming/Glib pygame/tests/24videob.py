from Glib import *

startdraw(400, 400)
s = loadVideo ("H:/introProgramming/chapter09/tests/knick.mpg")
if s != None:
    playVideo(s)
enddraw()