def factorial2(num):
  prod = 1
  for x in range(1,num+1):
    prod = prod * x
  return prod

result = factorial2(5)
print('The factorial of 5 =', result)

