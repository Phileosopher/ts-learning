import random

correct = 0
for i in range(0,10):
    K = random.randint(10000, 1000000)  # Generate a new number
    print ("Prime or Not: Is the number ",K," prime? (yes or no)")
    answer = input()      # Read the user's choice
    isprime = "yes"
    for n in range(2,int(K/2)): #to iterate on the factors of the number
        if K%n == 0:      #to determine the first factor
            isprime = "no"          #to calculate the second factor
    if isprime=='yes':                  # else part of the loop
        print (K, 'is a prime number')
    else:
        print (K, 'is a composite number')
    if isprime==answer:
        print ("You are correct!")
        correct = correct + 1
    else:
        print ("You are incorrect.")
print ("You gave ",correct," right answers out of 10.")
