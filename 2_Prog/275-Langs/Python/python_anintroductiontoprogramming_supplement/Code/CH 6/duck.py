from math import *

class point:
    def __init__ (self, x, y):
        self.__x = x
        self.__y = y
    def getx (self):
        return self.__x
    def gety (self):
        return self.__y
    def setx (self, x):
        self.__x = x
    def sety (self, y):
        self.__yy = y
    def distance (self, p):
        d = (self.__x-p.getx())*(self.__x-p.getx()) + \
             (self.__y-p.gety())* (self.__y-p.gety())
        return sqrt(d)
    def move(self, dx, dy):
        self.__x = self.__x + dx
        self.__y = self.__y + dy
    def draw (self):
        print ("(", self.__x, ",", self.__y, ") ")

class triangle:
    def __init__ (self, p0, p1, p2):
        self.v0 = p0
        self.v1 = p1
        self.v2 = p2
        self.x = (p0.getx()+p1.getx()+p2.getx())/3
        self.y = (p0.gety()+p1.gety()+p2.gety())/3
    def getx(self):
        return (self.x)
    def gety(self):
        return (self.y)
    def set_vertices (self, p0, p1, p2):
        self.v0 = p0
        self.v1 = p1
        self.v2 = p2
    def get_vertices (self):
        return ( (self.v0, self.v1, self.v2) )
    def draw (self):
        print ("Triangle:")
        self.v0.draw()
        self.v1.draw()
        self.v2.draw()
        print ("[", self.x, ",", self.y, "]")
    def move (self, dx, dy):
        self.v0.move(dx, dy)
        self.v1.move(dx, dy)
        self.v2.move(dx, dy)
        self.x += dx
        self.y += dy


def moveaway (a, b):
    dx = a.getx()-b.getx()
    dy = a.gety()-b.gety()
    a.move (dx/10, dy/10)
    b.move (-dx/10, -dy/10)
    a.draw()
    b.draw()

v0 = point (10,10)
v1 = point (20,20)
v2 = point (10,20)
print (hasattr( v0, "getx"))


t = triangle (v0,v1,v2)
t.draw()
p = point (30, 30)
print ("Distance is", p.distance (t))
p.draw()
moveaway (p, t)
print ("Distance is", p.distance (t))
print ()
