# Test 11 - Audio
# sound file load, play, all audio options.

from Glib import *


startdraw(400, 300)
music = loadSound ("sun.ogg")
textsize (32)
text ("Sun Goes By", 100, 40)
data = soundData(music)
x = playSoundData(data)
enddraw()