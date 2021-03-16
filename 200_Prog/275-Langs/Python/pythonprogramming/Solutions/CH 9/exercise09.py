from Glib import *

class Anim:         # Simple animation class -----------------------
    def __init__ (self, v):
        self.vid = v         # Animation video
        self.n = v.length()*24      # Number of frames
        self.f = 0               # Current frame
        self.active = False      # Playing?
        self.delay = 1           # Current frame delay
        self.count = 100000      # How far into the delay are We?

    def draw (self):         # Draw the current frame and advance
        if self.active:
            if self.f > self.n:  # Loop
                f = 1
            self.vid.draw_frame(self.f)
            self.count = self.count + 1  # Delay?
            if self.count >= self.delay: # Do it
                self.f = self.f + 1      # Increment frame after count
                self.count = 0
            if (self.f >= self.n):       # Loop to 0 if at the end
                self.f = 0

    def setdelay (self, d):
        self.delay = d

    def start(self):
        self.active = True

    def stop (self):
        self.active = False

def draw ():
    a.draw()
    b.draw()
    c.draw()

startdraw(800, 531)
background = loadImage ("panel.jpg")
image (background, 0, 0)
av = Gvideo("launch.mpg")
av.locVideo(239, 284, 50, 45)
a = Anim(av)
bv = Gvideo ("ellipsis.mpg")
bv.locVideo (319, 258, 50, 45)
b = Anim(bv)
b.setdelay(100)
cv = Gvideo ("ellipsis.mpg")
cv.locVideo(319, 322, 50, 45)
c = Anim(cv)
c.setdelay(10)
a.start()
b.start()
c.start()
enddraw()