# Ball.py
import math
class Ball:
# Constructor/initializer
    def __init__(self, height, elasticity):
        self.height = height        # Initially the height from which the ball is dropped.
        self.e = elasticity         # How much energy is retained each bounce
        self.speed = 0.0            # Current speed of the ball, initially 0, down +
        self.a = 32.0               # Acceleration: G= 32 ft/sec^2

# What Java would call an accessor: not really needed.
    def getHeight(self):
        return self.height

# Calculate the new height and speed for a change in time of dt seconds.
    def delta (self, dt):
        startHeight = self.height               # Remember the state before dt
        startSpeed = self.speed
        s = 0.5*self.a*dt*dt + self.speed*dt    # Equation 1: position update
        self.height = self.height - s
        self.speed = self.speed + self.a*dt     # Equation 2: Speed update
        if self.height < 0:                     # The sign changed; bounce, when?
    # Equation 3: Solve the quadratic equation to find the time of bounce
            xt = (-startSpeed - math.sqrt(startSpeed*startSpeed +2*self.a*startHeight))/self.a
            if xt < 0:
                xt = (-startSpeed + math.sqrt(startSpeed*startSpeed +2*self.a*startHeight))/self.a
            print ("Bounces at time ", xt)
            self.speed = -(self.speed + self.a*xt)*self.e  # Equation 2 with elasticity
            self.height = -self.height * self.e            # Correct the height
            if self.e <0.03: self.e = 0.0
            else: self.e = self.e - 0.03
        elif startSpeed*self.speed < 0:    # Peak of the up ward bound, velocity changes sign
            self.speed = 0         # Speed is 0 at the top of the bounce
            print("Peak")
        print ("New speed is ", self.speed, " and height starts at ", self.height)
        if self.height<0.:
            self.height = 0.


class Screen:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.ppf = 3

    def draw (self, object, x, y):
        h = (int)(self.height-(y*self.ppf))
        for i in range (0, self.height*self.ppf):
            if i == h:
                for j in range(0, x):
                    print(" ", end="")
                print (object)
            else:
                print()
        for j in range(0,self.width): print ("_", end="")
        print()

b = Ball (12.0,  0.5)  # Initial height 12 feet, elasticity is 0.5
s = Screen (20, 40)

for i in range (0, 50):
    b.delta (0.1)   # Time increment is 0.1 seconds
