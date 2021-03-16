def root (x):
    y = x
    for i in range(1, 6):
        y = (y + x/y)/2.0
    return y


print (root(2.0))
print (root(0.04))


