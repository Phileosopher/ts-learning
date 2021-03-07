# Exercise 8.05

def writedict (d, s):
    f = open (s, "w")
    for (key,value) in d.items():
        f.write(key)
        f.write ("\n")
        f.write(value)
        f.write ("\n")
    f.close()

def readdict (s):
    d = {}
    f = open (s, "r")
    while True:
        k = f.readline()
        if k == "": return d
        v = f.readline()
        k = k.rstrip()
        v = v.rstrip()
        d[k] = v
    f.close()
    return d



dict = {}
while True:
    name = input("Enter the name of a person ")
    if name == "done": break
    city = input ("Enter the city where that person lives ")
    dict[name] = city

writedict (dict, "dout.txt")
dd = readdict("dout.txt")
print (dd.items())


