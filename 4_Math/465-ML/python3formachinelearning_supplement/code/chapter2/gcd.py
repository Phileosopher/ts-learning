
def gcd(num1, num2):
  if(num1 % num2 == 0):
    return num2 
  elif (num1 < num2):
    print("switching ", num1, " and ", num2)
    return gcd(num2, num1)
  else:
    print("reducing", num1, " and ", num2)
    return gcd(num1-num2, num2)

result = gcd(24, 10)
print("GCD of", 24, "and", 10, "=", result) 


