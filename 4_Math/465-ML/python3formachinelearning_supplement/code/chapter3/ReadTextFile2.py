count = 1
with open('sample.txt', 'rt') as f: 
  for line in f:
    print("Line",count,":",line)
    count = count + 1 

