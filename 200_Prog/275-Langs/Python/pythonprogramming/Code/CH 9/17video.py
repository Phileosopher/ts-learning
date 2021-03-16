from Glib import *

def draw ():
    global vid
    background (0, 200, 190)         # Clear the background, set to aqua.
    if isVideoPlaying(vid):          # Playing? Print an indicator
        text ("playing", 10, 40)
    else:
        text ("Not playing", 10, 40)
    whr = whereVideo(vid)                      # Current time of play
    text ("Frame "+str(getVideoFrame(vid)), 10, 60)   # Current frame
    text ("Length "+ str(whr)+" of "+str(lengthVideo(vid)), 40, 370)

def keyPressed(k):
    global vid
    if k == K_p:            # Key pressed was a ‘p’
        pauseVideo(vid)     # Pause

startdraw(500, 500)
vid = loadVideo("carclub2.mpg")        # Load the car club video
locVideo(vid, 100, 100, 200, 200)      # Position it at (100, 100)
playVideo(vid)                         # Play it.
enddraw()
