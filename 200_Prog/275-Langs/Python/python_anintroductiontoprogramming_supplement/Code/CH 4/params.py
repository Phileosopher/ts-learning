# Passing a function as a parameter.


def print0():
    print ("Zero")
def print1():
    print ("One")
def print2():
    print ("Two")
def print3():
    print("Three")

def quad1 (x):
    return x*x -3*x + 12

def deriv ( x):
    def quad (x):
        return x*x -3*x + 12
    return quad(x)
#    return (f(x+0.001)-f(x-0.001))/0.002

def df (x):
    return 2*x - 3

def getPrintFun (a):		# Return a function to print a numeric value 0..3
    if a == 0:
        return print0
    elif a == 1:
    	return print1
    elif a == 2:
    	return print2
    else:
    	return print3

def derivative (f, x):
    delta = 1.0
    old = f(x)
    h = 0.5
    while delta > 0.000001:
        dx = (f(x+h)-f(x))/h
        delta = abs(old-dx)
        old = dx
        h = h / 2
    return dx

# Search the list for the given name, recursively.
def searchr (name, nameList):
    n = len(nameList)            # How many elements in this list?
    m = int(n/2)
    if n==1 and nameList[0]!=name:
        return False
#    print ("Target is ", name, "n=", n, "m=", m, "Mid is ", nameList[m])
    if name < nameList[m]:       # target name is in the first half
        return searchr (name, nameList[0:m])  # Search the first half
    elif name > nameList[m]:     # target must be in the second half
        return searchr (name, nameList[m:n])  # Search the second half
    else:
        return True

nameList = ["Allen", "Atkins", "Baker", "Binford", "Capra", "Donovan", "Elford", "Fremont", "Gordo", "Howard", "Innes", "Jackson"]
print (searchr("Smith", nameList))
print(searchr("Depp", nameList))
print(searchr("aaa", nameList))

for i in range(0,8):
    print (searchr(nameList[i], nameList), nameList[i])
x = 3.0
print (x, quad1(x), df(x), derivative(quad1, x))




