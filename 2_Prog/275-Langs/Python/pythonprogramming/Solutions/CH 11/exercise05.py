import math

def xinverse (x):
    return 1/x

def simpson (f, a, b):
    c = (b-a)/6
    return c * (f(a)+4*f((a+b)/2) + f(b))

def integral (f, a, b):
    sum = 0.0
    dx = (b-a)/100.0
    x = a
    for i in range (0, 100):
        sum = sum + simpson (f, x, x+dx)
        x = x + dx
    return sum

def log (v):
    return integral (xinverse, 1.0, v)

sum = 0.0
for i in range (2, 100):
    print (log(i), math.log(i))
