print("Enter a number: ")
num = int( input() )
isprime = True
for i in range(2,int(num/2)): #to iterate on the factors of the number
    if num%i == 0:      #to determine the first factor
        isprime = False #to calculate the second factor
if isprime:             # else part of the loop
    print (num, 'is a prime number')
else:
    print (num, 'is a composite number')



