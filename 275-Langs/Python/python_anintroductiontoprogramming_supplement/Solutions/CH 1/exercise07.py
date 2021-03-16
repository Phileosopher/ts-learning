# Exercise 1.7

print ("=========== Sort Three Numbers ===========")
print()

s = input ("Enter a: ")
a = float(s)
s = input ("Enter b: ")
b = float(s)
s = input ("Enter c: ")
c = float(s)

if a>=b and a>=c:
    if b>=c:
        print (a, b, c)
    else:
        print (a, c, b)
elif b>=a and b>=c:
    if a>=c:
        print (b, a, c)
    else:
        print (b, c, a)
elif c>=a and c>=b:
    if a>b:
        print (c, a, b)
    else:
        print (c, b, a)
else:
    print ("What?")

print ("--------------------------------------------------------")

