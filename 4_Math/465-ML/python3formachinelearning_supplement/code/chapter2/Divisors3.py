def divisors(num):
  count = 1
  div = 2
  while(div < num):
    if(num % div == 0):
      count = count + 1
    div = div + 1
  return count

result = divisors(12)

if(result == 1):
  print('12 is prime')
else:
  print('12 is not prime')

