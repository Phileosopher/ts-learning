# Differentiation
from math import *
n0 = 0
n1 = 0

def f1 (x):         # Sample function for differentiation test
    return (x-1)*(x-1)*(x-1)

def df1 (x):        # Derivative of f1
    return 3*x*x - 6*x+3

def intf1 (x0, x1):
    return f1(x1) - f1(x0)

def f2 (x):         # Sample function for differentiation test
    return x*x + 3.0*x + 4

def intf2(x0, x1):
    return f2(x1)-f2(x0)

def df2 (x):        # derivative of f2
    return 2*x + 3

def f3 (x):
    return sqrt(x)

def df3 (x):
    return 1.0/(2*sqrt(x))

def intf3(x0, x1):
    return f3(x1)-f3(x0)

def deriv1 (f, x, delta=0.0001, niter=20):  # Two point derivative
    global n0
    h = 0.001
    n = 0
    dx = f(x)
    while n<niter:
        try:
            old_dx = dx
            dx = (f(x+h)-f(x-h))/(2*h)
            n = n + 1
            if abs(dx-old_dx) < delta:
                n0 = n
                return dx
        except:
            print ("Exception is deriv1")
            return 0

def deriv2 (f, x, delta=0.0001, niter=20):  # Four point derivative
    global n1
    h = 0.001
    n = 0
    dx = f(x)
    while n<20:
        try:
            old_dx = dx
            dx = (-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)
            n = n + 1
            if abs(dx-old_dx) < delta:
                n1 = n
                return dx
        except:
            print ("Exception is deriv2")
            return 0

def trap0 (f, x0, x1, n):  # Slow
    dx = (x1-x0)/n
    xa = x0
    xb = x0+dx
    sum = 0
    for i in range(0, n):
        f0 = f(xa)
        f1 = f(xb)
        sum = sum + dx*(f1+f0)/2
        xa = xa + dx
        xb = xb + dx
    return sum

def trapezoid (f, x0, x1, delta=0.0001, niter=1024):
    n = 4
    delta = 0.0001
    resold = trap0(f, x0, x1, 2)
    resnew = trap0(f, x0, x1, 4)
    while abs(resnew-resold) > delta:
        if n>niter: break
        resold = resnew
        n = n * 2
        resnew = trap0 (f, x0, x1, n)
    return resnew

def trap1 (f, x0, x1, n):  # Fast
    dx = (x1-x0)/n
    sum = f(x0)/2
    xa = x0
    for i in range(1, n):
        xa = xa + dx
        sum = sum + f(xa)
    sum = sum + f(x1)/2
    return sum*dx

x = trapezoid (df2, 1, 5.)
y = intf2(1, 5.)
print ("Real = ", y, " numerical = ", x)