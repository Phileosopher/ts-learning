import time

list = [19872, 87656, 10982, 18756, 56344, 29765, 12856, 12534, 88768, 90012]
t0 = time.clock()
for i in range (0,10000):
    if 90012 in list:
        found = True
t1 = time.clock()
print ("Time was ", (t1-t0)/10000)

index = -1
target = 90012
t0 = time.clock()
for i in range (0,10000):
    for i in range(0,len(list)):
        if  list[i] == target:
            index = i
            break
t1 = time.clock()
# If the value of index is >= 0 then it was found.
print ("Time was ", (t1-t0)/10000)
