from Glib import *

startdraw()
s = loadSound ("song.wav")
if s == None:
    print ("No such sound file.")
else:
    playSound(s)
enddraw()