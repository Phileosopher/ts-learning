from Glib import *

class Anim:         # Simple animation class -----------------------
    def __init__ (self, x, y):
        self.frames = []         # Animation frames, images
        self.xpos = x            # X,Y position on the window
        self.ypos = y
        self.n = 0               # Number of frames
        self.f = 0               # Current frame
        self.active = False      # Playing?
        self.delay = 1           # Current frame delay
        self.count = 100000      # How far into the delay are We?

    def draw (self):         # Draw the current frame and advance
        if self.active:
            image (self.frames[self.f], self.xpos, self.ypos)
            self.count = self.count + 1  # Delay?
            if self.count >= self.delay: # Do it
                self.f = self.f + 1      # Increment frame after count
                self.count = 0
            if (self.f >= self.n):       # Loop to 0 if at the end
                self.f = 0

    def setdelay (self, d):
        self.delay = d

    def getframes (self, s1, s2):
        self.frames = []
        for i in range (0, 100):
            if i<10:
                s = s1 + "0"+str(i) + s2
                print ("Reading ", s)
            elif i<100:
                s = s1 + str(i) + s2
            x = loadImage (s)
            if x == None:
                self.n = i
                print ("Saw ", self.n, " frames.")
                break
            self.frames = self.frames + [x,]


    def start(self):
        self.active = True

    def stop (self):
        self.active = False

def draw ():
    a.draw()
    b.draw()
    c.draw()

startdraw(800, 531)
background = loadImage ("images/800px-STSCPanel.jpg")
image (background, 0, 0)
a = Anim(239, 284)
a.getframes ("images/g1", ".gif")
b = Anim (319, 258)
b.getframes ("images/g2", ".jpg")
b.setdelay(100)
c = Anim (319, 322)
c.getframes ("images/g3", ".gif")
c.setdelay(10)
a.start()
b.start()
c.start()
enddraw()