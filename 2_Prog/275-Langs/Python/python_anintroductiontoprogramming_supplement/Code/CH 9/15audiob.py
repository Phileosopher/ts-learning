from Glib import *

def keyPressed(k):
    global volume, s
    if k == K_PLUS:
        volume = volume+.1
    elif k == K_MINUS:
        volume = volume-.1
    if volume<0: volume = 0
    if volume>1: volume = 1
    volumeSound(s, volume)
    print (volume)

startdraw()
s = loadSound ("song.wav")
volume = 1.0
volumeSound (s, volume)
if s == None:
    print ("No such sound file.")
else:
    playSound(s)
enddraw()
