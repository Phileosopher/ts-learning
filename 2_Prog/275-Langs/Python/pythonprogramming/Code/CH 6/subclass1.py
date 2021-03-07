class gobject:
    position = (0, 0, 0)       # Object position in 3D
    visual = None              # Graphics that represent the object
    def __init__ (self, pos, vis):
        self.position = pos
        self.visual = vis
        print ("gobject init")
    def getPosition (self):
        return self.position
        print ("getPosition")
    def setPosition(self, p):
        self.position = p
        print ("setPosition")
    def setVisual(self, v):
        self.visual = v
        print ("setVisual")
    def draw (self):
        print("Draw")

class mobject (gobject):
    speed = (0, 0, 0)  # Speed in pixels per frame the x,y,z directions
    def __init__ (self, s):
        self.speed = s
        super().__init__((10,10,10), None)
        print ("mobject init")
    def getSpeed(self):
        print ("getSpeed")
        return self.speed
    def setSpeed(self, s):
        print ("setSpeed")
        self.speed = s
    def move(self):
        self.position = self.position + (1, 1, 0)
        print ("Move")
    def collision(self, gobject):
        print ("collision")

g = gobject ((12, 12,12), None)
m = mobject((13,13,13))
print (m.getPosition())
m.move()
m.draw()
print("Is m a gobject? ", isinstance (m, gobject))
print ("Is m a subclass of gobject? ", issubclass(mobject, gobject))
print ("Is m a subclass of mobject? ", issubclass(mobject, mobject))
print (m.__class__)
print (m.__class__.__name__)