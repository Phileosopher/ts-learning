# Exercise 1.9

print ("=========== Calculate PI ===========")
print()

p = 4/1
print ("Term 1, pi = ", p)
p = p - 4/3
print ("Term 2, pi = ", p)
p = p + 4/5
print ("Term 3, pi = ", p)
p = p - 4/7
print ("Term 4, pi = ", p)
p = p + 4/9
print ("Term 5, pi = ", p)
p = p -4/11
print ("Term 6, pi = ", p)
p = p + 4/13
print ("Term 7, pi = ", p)
p = p - 4/15
print ("Term 8, pi = ", p)
p = p + 4/17
print ("Term 9, pi = ", p)
p = p -4/19
print ("Term 10, pi = ", p)
p = p + 4/21
print ("Term 11, pi = ", p)
p = p - 4/23
print ("Term 12, pi = ", p)
p = p + 4/25
print ("Term 13, pi = ", p)
p = p - 4/27
print ("Term 14, pi = ", p)
p = p + 4/29
print ("Fifteen terms yields pi = ", p)

p = p - 4/31 + 4/33 - 4/35 + 4/37 - 4/39 + 4/41
print ("Twenty one terms yields pi = ", p)

# Note: It takes about 2500 terms to reach 3.141
# Here's a loop ...
# sign = 1
# den = 1
# p = 0.0
# for i in range (1, 22):
#     p = p + sign*4/den
#     sign = -sign
#     den = den + 2
#     print ("Iteration ", i, "pi = ", p)

print ("--------------------------------------------------------")

