def sum(*values):
  sum = 0
  for x in values:
    sum = sum + x
  return sum

values1 = (1, 2)
s1 = sum(*values1)
print('s1 = ',s1)

values2 = (1, 2, 3, 4)
s2 = sum(*values2)
print('s2 = ',s2)

