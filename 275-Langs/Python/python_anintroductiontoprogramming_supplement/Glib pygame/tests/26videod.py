from Glib import *

def draw ():
    global frame, v, wid, ht, x
    background (200)
    s = v.set_frame_number(frame)
    image (s, 0, 0)

    for i in range (0,wid):
        for j in range(0,ht):
            p = getVideoPixel (v, i, j)
            g = grey(p)
            if g<t:
                fill (0)
            else:
                fill (255)
            point (i, j+ht)
    frame = frame + 1
    fill (0)
    text ("Original: Frame"+str(frame), 10, 30)
    text ("Thresholded: Frame "+str(frame), 10, ht+30)

s = videoSize("carclub2.mpg")
print ("Size ", s)
startdraw(s[0],s[1]*2)
v = Gvideo ("carclub2.mpg")
frame = 1
wid = s[0]
ht = s[1]
t = 100
locVideo(v, 0, 0, wid, ht)

enddraw()