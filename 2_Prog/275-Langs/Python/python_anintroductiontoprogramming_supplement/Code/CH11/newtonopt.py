# Newton optimization 1D
from math import *

def deriv (f, x, delta=0.0001, niter=20):  # Four point derivative
    global n1
    h = 0.001
    n = 0
    dx = f(x)
    while n<20:
        try:
            old_dx = dx
            dx =(-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)
            n = n + 1
            if abs(dx-old_dx) < delta:
                n1 = n
                print ("Dx is ", dx)
                return dx
        except:
            print ("Exception deriv")
            return 0

def derivsecond (f, x, delta=0.0001, niter=20):  # Second derivative of f at x
    global n1
    h = 0.001
    n = 0
    dx = f(x)
    while n<niter:
        try:
            old_dx = dx
            dx = ( f(x+h) - 2*f(x) + f(x-h) )/(h*h)
            n = n + 1
            if abs(dx-old_dx) < delta:
                n1 = n
                return dx
        except:
            print ("Exception derivsecond")
            return 0

def newtonopt (f, x0, x1, delta=0.0001, niter=20):
    x = (x0+x1)/2
    fa = 1000.0
    fb = f(x)
    i = 0
    print ("Iteration 0: x=", x, " f=", fb)
    while (abs(fa-fb) > delta):
        fa = fb
        x = x - deriv(f, x)/derivsecond(f, x)
        fb = f(x)
        i = i + 1
        print ("Iteration ", i, ": x=", x, " f=", fb)
        if i>niter:
            return 0

def fun (x):
    return x*x-2*x + 8
   # return sin (x*3.1415/180.0)

print ("Newton optimization: ")
for i in range (-10, 10):
    print (i, fun(i))
z = newtonopt (fun, 0, 180)
print (z)