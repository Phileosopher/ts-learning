# Test 11 - display a video
# video load, play, all video options. locVideo.
mov = None

from Glib import *

c = videoSize ("carclub2.mpg")

startdraw(800, 800)
mov = loadVideo ("carclub2.mpg")
locVideo (mov, 300, 300, 200, 200)
playVideo(mov)
setVideoVolume (mov, 1.0)
enddraw()