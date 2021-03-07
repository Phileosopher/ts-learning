# Differentiation
from math import *
n0 = 0
n1 = 0

def f1 (x):         # Sample function for differentiation test
    return (x-1)*(x-1)*(x-1)

def df1 (x):        # Derivative of f1
    return 3*x*x - 6*x+3

def f2 (x):         # Sample function for differentiation test
    return x*x + 3.0*x + 4

def df2 (x):        # derivative of f2
    return 2*x + 3

def f3 (x):
    return sqrt(x)
def df3 (x):
    return 1.0/(2*sqrt(x))

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
            h = h/2
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
            h = h/2
            if abs(dx-old_dx) < delta:
                n1 = n
                return dx
        except:
            print ("Exception is deriv2")
            return 0

for i in range (1,20):
    x = i*1.0
    f = f1(x)
    df = df1(x)
    mydf = deriv1 (f1, x)
    mydf2 = deriv2(f1, x)
    print (f, df, mydf, n0, "   ", mydf2, n1)