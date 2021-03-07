# Exercise 2.3

print ("Exercise 2.3 - Zeno's Paradox")
print ("=============================")
increment = 1./2.
val = increment
for i in range(1,21):
    print ("Iteration (step)", i, " gets Achilles to ", val)
    increment = increment/2.0
    val = val + increment
print ("Last step gets to ", val)
print ("-------------------------------------------------")

# An alternative ...
# x = 2
# sum = 0
# for i in range(0,20):
#     sum = sum + 1/x
#     x = x*2
#     print ("After ",i," sum is ", sum)
#
# Sums to 1.0

# Output should be:
# Exercise 2.3 - Zeno's Paradox
# =============================
# Iteration (step) 1  gets Achilles to  0.5
# Iteration (step) 2  gets Achilles to  0.75
# Iteration (step) 3  gets Achilles to  0.875
# Iteration (step) 4  gets Achilles to  0.9375
# Iteration (step) 5  gets Achilles to  0.96875
# Iteration (step) 6  gets Achilles to  0.984375
# Iteration (step) 7  gets Achilles to  0.9921875
# Iteration (step) 8  gets Achilles to  0.99609375
# Iteration (step) 9  gets Achilles to  0.998046875
# Iteration (step) 10  gets Achilles to  0.9990234375
# Iteration (step) 11  gets Achilles to  0.99951171875
# Iteration (step) 12  gets Achilles to  0.999755859375
# Iteration (step) 13  gets Achilles to  0.9998779296875
# Iteration (step) 14  gets Achilles to  0.99993896484375
# Iteration (step) 15  gets Achilles to  0.999969482421875
# Iteration (step) 16  gets Achilles to  0.9999847412109375
# Iteration (step) 17  gets Achilles to  0.9999923706054688
# Iteration (step) 18  gets Achilles to  0.9999961853027344
# Iteration (step) 19  gets Achilles to  0.9999980926513672
# Iteration (step) 20  gets Achilles to  0.9999990463256836
# Last step gets to  0.9999995231628418
# -------------------------------------------------
