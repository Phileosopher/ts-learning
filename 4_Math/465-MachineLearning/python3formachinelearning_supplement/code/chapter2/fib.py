
def fib(num):
  if (num == 0):
    return 1
  elif (num == 1):
    return 1
  else:
    return fib(num-1) + fib(num-2)

result = fib(10)
print('Fibonacci value of 10 =', result)

