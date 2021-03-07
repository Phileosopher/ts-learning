
divList = ""

def divisors(num):
  global divList 
  primes = ""
  div = 2

  while(num > 1):
    if(num % div == 0):
      divList = divList + str(div) + " "
      num = num / div
    else:
      div = div + 1
  return divList

result = divisors(12)
print('The divisors of',12,'are:',result)

