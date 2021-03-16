# Exercise 2.5

print ("Earnings for WidgetCorp for 2016")
print ("   Dollars for each quarter   ")
print (" ==============================")
q1 = 190000
q1scaled = int(q1/20000)
print ("Q1: ", end="")
for k in range(1, q1scaled):
    print ('#', end='')
print ("     ", q1)

q2 = 340000
q2scaled = int(q2/20000)
print ("Q2: ", end="")
for k in range(1, q2scaled):
    print ('#', end='')
print ("     ", q2)

q3 = 873000
q3scaled = int(q3/20000)
print ("Q3: ", end="")
for k in range(1, q3scaled):
    print ('#', end='')
print ("     ", q3)

q4 = 439833
q4scaled = int(q4/20000)
print ("Q4: ", end="")
for k in range(1, q4scaled):
    print ('#', end='')
print ("     ", q4)

# Output should be:
# Earnings for WidgetCorp for 2016
#    Dollars for each quarter
#  ==============================
# Q1: ########      190000
# Q2: ################      340000
# Q3: ##########################################      873000
# Q4: ####################      439833