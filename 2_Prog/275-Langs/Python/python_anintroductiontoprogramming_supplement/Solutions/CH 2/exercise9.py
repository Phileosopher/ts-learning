# Exercise 2.9

print ("Exercise 2.9 - Square Root")
print ("=============================")
print ("Enter a number: ")
b = float(input())

try:
    x = b/2
    for i in range(1,20):
        x = (x + b/x)/2
        if abs(b-x*x) < 0.001:
            break;
    if abs(x*x-b)<0.1:
        print ("Square root of ", b, " is ", x)
    else:
        print ("No real square root of ", b, "was found.")
except:
    print ("No real square root of ", b, "can be found.")
print ("-------------------------------------------------")


