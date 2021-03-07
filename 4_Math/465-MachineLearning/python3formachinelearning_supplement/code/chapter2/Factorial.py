
def factorial(num):
  if (num > 1):
    return num * factorial(num-1) 
  else:
    return 1

result = factorial(5)
print('The factorial of 5 =', result)

