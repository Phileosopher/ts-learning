# Exercise 2.7

print ("=========== Making Change ===========")
print()

change = input ("Enter an amount, integer, <100: ")
total = int(change)
coin = 25   # To use 50 cent piece set this to 50
while total>4:
    k = total//coin
    if k>0:
        print (k, "coins of value", coin)
        total = total - k*coin
    if coin==25:
        coin = 10
    else:
        coin = coin//2
if total > 0:
    print (total, " pennies")

print ("--------------------------------------------------------")


# Output:
# Draw histogram for WidgetCorp Earnings in 2016.
# Enter earning for the first quarter: 900000
# Enter earning for the second quarter:874000
# Enter earning for the third quarter:200000
# Enter earning for the fourth quarter:439000
# Earnings for WidgetCorp for 2016
#    Dollars for each quarter
#  ==============================
# Q1: ############################################      900000
# Q2: ##########################################      874000
# Q3: #########      200000
# Q4: ####################      439000