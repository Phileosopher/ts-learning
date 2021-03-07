# Exercise 2.1

var1 = 12
var2 = 100
var3 = -2
var4 = 0

print ("a.")
while var1 < var2:
    print (var1)
    var1 = var1 + 30
print ("--------------------------------")

var1 = 12
var2 = 100
var3 = -2
var4 = 0
print ("b.")
while var1 < var2:
    print (var1)
    var1 = var1 * 2
print ("--------------------------------")

var1 = 12
var2 = 100
var3 = -2
var4 = 0
print ("c.")
while var1 > 0:
     var4 = var4 + 1
     var1 = var1 - 1
print (var1, var2)
print ("--------------------------------")

var1 = 12
var2 = 100
var3 = -2
var4 = 0
print ("d.")
while var1 > 0:
     var4 = var4 + 1
     var1 = var1 - var4
print (var1, var2)
print ("--------------------------------")

var1 = 12
var2 = 100
var3 = -2
var4 = 0
print ("e.")
while var1 < var3:
    print ("*", end="")
    var3 = var3 + 2
print ("--------------------------------")

var1 = 12
var2 = 100
var3 = -2
var4 = 0
print ("f.")
while var2 > var1*var4:
     var1 = var1 + 1
     var4 = var4 + 1
print (var1, var2)
print ("--------------------------------")

# Output should be:
# a.
# 12
# 42
# 72
# --------------------------------
# b.
# 12
# 24
# 48
# 96
# --------------------------------
# c.
# 0 100
# --------------------------------
# d.
# -3 100
# --------------------------------
# e.
# --------------------------------
# f.
# 18 100
# --------------------------------