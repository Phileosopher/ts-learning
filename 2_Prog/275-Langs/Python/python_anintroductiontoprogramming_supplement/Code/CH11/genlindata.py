# Generate data to test regression program
from random import *

def f(x):
    y = 3*x -2
    return y

x = 0
for i in range (0, 100):
    y = f(x) + random ()*3-1.5
    xx = x + random( )*2-1
#    print ("  xpoint (", xx, ",", y, ");")
    print (xx, ",", y)
    x = x + 0.1