from Glib import *

class Anim:
    def __init__ (self, x, y):
        self.frames = []
        self.xpos = x
        self.ypos = y
        self.n = 0
        self.f = 0
        self.active = False
        self.delay = 1
        self.count = 100000

    def draw (self):
        if self.active:
            image (self.frames[self.f], self.xpos, self.ypos)
            self.count = self.count + 1
            if self.count >= self.delay:
                self.f = self.f + 1
                self.count = 0
            if (self.f >= self.n):
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