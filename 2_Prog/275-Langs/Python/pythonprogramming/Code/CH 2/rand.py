maxv = 1
maxcount = 0
for k in range(1, 10000):
    count = 0;
    for n in range (2, int(k/2)): # Divide K by all numbers < K/2
        if k%n == 0:              # If the remainder is 0 then n
            count = count + 1
    if count > maxcount:		# A new maximum
        maxcount = count
        maxv = k
print ("The most divisors is ", maxv, " with ", maxcount)
print ("They are:")
count = 1
k = maxv
for n in range (1, int(k/2)):
    if k%n == 0:
        print (count, ". ", n, " and ", k//n)
        count = count + 1


