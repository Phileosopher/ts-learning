def f2 (x):         # Sample function for differentiation test
    return x*x

def simpson (f, a, b):
    c = (b-a)/6
    return c * (f(a)+4*f((a+b)/2) + f(b))

def simpson_rule(a,b):
  #Approximation by Simpson's rule
  c=(a+b)/2.0
  h=abs(b-a)/2.0
  return h*(f2(a)+4.0*f2(c)+f2(b))/3.0

print (simpson_rule (1, 5))

sum = 0.0
for i in range (1, 5):
    sum = sum + simpson (f2, i, i+1)
print (sum)