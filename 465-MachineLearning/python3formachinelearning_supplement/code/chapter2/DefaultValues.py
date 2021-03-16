def numberFunc(a, b=10):
  print (a,b)

def stringFunc(a, b='xyz'):
  print (a,b)

def collectionFunc(a, b=None):
  if(b is None):
     print('No value assigned to b')

numberFunc(3)
stringFunc('one')
collectionFunc([1,2,3])

