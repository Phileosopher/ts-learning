
def cube(x): return x*x*x
def fourth(x): return x*x*x*x

x1 = map(cube,  range(1, 5))
x2 = map(fourth, range(1, 5))

print(x1)
print(x2)

