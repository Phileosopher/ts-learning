import random

def hash (s, size):
    sum = 0
    for i in range (0, len(s)):
        sum = sum + ord(s[i])
    sum = sum % size
    return sum

def djb2 (s, size):
        sum = 5381
        for i in range (0, len(s)):
            sum = sum*33 + ord(s[i])
        sum = sum%size
        return sum

def sdbm (s, size):
    hash = 0
    for i in range (0, len(s)):
        hash = ord(s[i]) * 65599 + hash
    return hash%size

str = "abcdefghijklmnopqrstuvwxyz ."

d1 = [0 for i in range(0,60)]
d2 = [0 for i in range(0,60)]
d3 = [0 for i in range(0,60)]

for i in range (0, 60):
    c = ""
    for j in range (0,43):
        c = c +  str[random.randint(0,27)]
    x = hash(c, 60)
    d1[x] = d1[x] + 1
    x = djb2(c, 60)
    d2[x] = d2[x] + 1
    x = sdbm(c, 60)
    d3[x] = d3[x] + 1

zeros1 = 0
zeros2 = 0
zeros3 = 0
for i in range (0, 60):
    if d1[i] == 0:
        zeros1 = zeros1 + 1
    if d2[i] == 0:
        zeros2 = zeros2 + 1
    if d3[i] == 0:
        zeros3 = zeros3 + 1

avg1 = 0
n1 = 0
avg2 = 0
n2 = 0
avg3 = 0
n3 = 0
for i in range (0, 60):
    if d1[i] != 0:
        n1 = n1 + 1
        avg1 = avg1 + d1[i]
    if d2[i] != 0:
        n2 = n2 + 1
        avg2 = avg2 + d2[i]
    if d3[i] != 0:
        n3 = n3 + 1
        avg3 = avg3 + d3[i]
avg1 = avg1/n1
avg2 = avg2/n2
avg3 = avg3/n3

print ("                           Hash                    DJB2                   SDBM")
print ("Zero cells                 ",zeros1, "                    ", zeros2, "                    ", zeros3)
print ("Averge occupancy  ", avg1,  "     ", avg2,   "     ", avg3)
