# Exercise 3.1
str1 = "okra is the closest thing to nylon i've ever eaten."
str2 = "pull the string, and it will follow wherever you wish."
str3 = "let out a little more string on your kite."
str4 = "every string is a different color, a different voice."
vowels = 'aeiou'

print ("a.", end="")
for i in range(0,len(str3)):
    print (str3[i], end='')
print()
print(" ----------------------------------------- ")

print ("b.", end="")
for i in range(0,len(str3)):
    print (i, end='')
print()
print(" ----------------------------------------- ")

print ("c.", end="")
for i in range(0,len(str3)):
    print (str2[i], end='')
print()
print(" ----------------------------------------- ")

print ("d.", end="")
for i in str3:
    print (i, end='')
print()
print(" ----------------------------------------- ")

print ("e.", end="")
for i in str3:
    if i in vowels:
        print(i, end='')
print()
print(" ----------------------------------------- ")

print ("f.", end="")
for i in str1:
    if not(i in vowels):
        print(i, end='')
print()
print (" =================================================")

# Results:
# a.let out a little more string on your kite.
#  -----------------------------------------
# b.01234567891011121314151617181920212223242526272829303132333435363738394041
#  -----------------------------------------
# c.pull the string, and it will follow wherev
#  -----------------------------------------
# d.let out a little more string on your kite.
#  -----------------------------------------
# e.eouaieoeioouie
#  -----------------------------------------
# f.kr s th clsst thng t nyln 'v vr tn.
#  =================================================