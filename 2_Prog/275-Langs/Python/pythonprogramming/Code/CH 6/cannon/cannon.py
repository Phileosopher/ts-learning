# Cannon game
from math import *

# The ball class
class Ball:
    def __init__ (self, x, y, dx, dy, name, other):
        self.xPos = x
        self.yPos = y
        self.xSpeed = dx
        self.ySpeed = dy
        self.gravity = 1.0
        self.name = name
        self.other = other

    def testCollision (self):
        global done
        d = self.xPos-self.other.x
        if d<0: d = -d
        if d < 1.0:
            done = True

    def step (self): # One time step
        self.xPos = self.xPos + self.xSpeed
        self.yPos = self.yPos + self.ySpeed
        self.ySpeed = self.ySpeed - self.gravity
        if self.yPos < 0:
            self.xSpeed = 0
            self.xSpeed = 0
            self.gravity = 0
            self.yPos = 0
            self.testCollision()


class Cannon:
    def __init__ (self, x, y, other):
        self.x = x
        self.y = y
        self.other = other
        self.ball = None

    def fire (self, angle, power):
        dy = sin(angle * 3.1415/180.0)
        dx = cos(angle * 3.1415/180.0)
        self.ball = Ball(self.x, self.y, dx*power/10.0, dy*power/10.0,
                         "Cat", self.other)

    def step (self):
        if self.ball != None:
            (self.ball).step()

class Screen:
    def __init__(self, a, b):
        self.height = 20
        self.width = 80
        self.player = 1
        self.cat = b

    def draw(self):
        global done
        for i in range (0,self.height+1):
            if player.ball != None:
                ballj = (int)(player.ball.xPos)
                balli = (int)(player.ball.yPos)
                if self.height-balli<0:
                    done = True
                    return
            else:
                ballj = balli = -1

            for j in range (0, self.width):
                if (int)(player.x)==j and (int)(player.y) == self.height-i:
                    print ("/", end="")
                elif ballj==j and balli==self.height-i:
                   print ("o", end="")
                elif self.cat.y==self.height-i and self.cat.x==j:
                    print("Y", end="")
                else:
                    print (" ", end="")
            print ("")
        print ("    ", end="")
        for i in range (0, self.width):
                print ("-", end="")
        print()
        print (
            "    01234567890123456789012345678901234567890123456789012345678901234567890")

cat = Cannon (60, 0, None)
player = Cannon (12, 0, cat)
scr = Screen(player, cat)
player.fire (42, 65)
done = False
while not done:
    player.step()
    scr.draw()
