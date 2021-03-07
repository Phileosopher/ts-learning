def divisors(num):
  div = 2

  while(num > 1):
    if(num % div == 0):
      print("divisor: ", div)
      num = num / div 
    else:
      div = div + 1
  print("** finished **")

divisors(12)

