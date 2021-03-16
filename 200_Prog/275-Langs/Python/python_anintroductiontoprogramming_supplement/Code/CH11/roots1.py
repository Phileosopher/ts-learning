# Roots of a function
def objective (x):
#    return (x-1)*(x-1)*(x-1)   # Root at x=1
    return x*x+3.0*x + 4

def deriv (x):
#    return 3*x*x - 6*x+3
    return 2*x+3.0

# Range is -2 to +12
x = 5.
fx = 1000.
delta = 0.000001
print ("Step 0: x=", x, " obj = ", objective(x))
i = 1
while abs(fx) > delta:
    f = objective(x)
    ff = f/deriv(x)
    x = x - ff
    fx = objective(x)
    print ("Step ",i,": x=", x, " obj = ", fx)
    i = i + 1
    if i>50:
        break


