# Roots of a function
def objective (x):
#    return (x-1)*(x-1)*(x-1)   # Root at x=1
    return x*x+3.0*x + 4

def deriv (x):
#    return 3*x*x - 6*x+3
    return 2*x+3.0

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


# Range is -2 to +12
x = 5.
fx = 1000.
delta = 0.000001
print ("Step 0: x=", x, " obj = ", objective(x))
i = 1
while abs(fx) > delta:
    f = objective(x)
    ff = f/deriv2(objective, x)
    x = x - ff
    fx = objective(x)
    print ("Step ",i,": x=", x, " obj = ", fx)
    i = i + 1
    if i>50:
        break


