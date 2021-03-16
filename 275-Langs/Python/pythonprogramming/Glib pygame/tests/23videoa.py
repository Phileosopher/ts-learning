from Glib import *

def draw ():
    global vid
    background (0, 200, 190)
    if isVideoPlaying(vid):
        text ("playing", 10, 40)
    else:
        text ("Not playing", 10, 40)
    whr = whereVideo(vid)
    text ("Frame "+str(getFrameNumber(vid)), 10, 60)
    text ("Length "+ str(whr)+" of "+str(lengthVideo(vid)), 40, 370)

def keyPressed(k):
    global vid
    if k == K_p:
        pauseVideo(vid)

startdraw(500, 500)
vid = loadVideo("carclub2.mpg")
locVideo(vid, 100, 100, 200, 200)
playVideo(vid)
enddraw()