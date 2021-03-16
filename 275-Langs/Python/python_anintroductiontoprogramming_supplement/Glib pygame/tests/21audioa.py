from Glib import *

startdraw(300, 200)
s = loadSound ("song.wav")
if s == None:
    print ("No such sound file.")
else:
    playSound(s)
text ("Song: 'Moving On' by Michael Becker", 10, 100)
enddraw()