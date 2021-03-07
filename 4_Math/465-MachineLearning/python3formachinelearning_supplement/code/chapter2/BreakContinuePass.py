print('first loop')
for x in range(1,4):
  if(x == 2):
    break
  print(x)

print('second loop')
for x in range(1,4):
  if(x == 2):
    continue 
  print(x)

print('third loop')
for x in range(1,4):
  if(x == 2):
    pass 
  print(x)

