x = 'This is a string that contains abc and Abc'
y = 'abc'
identical = 0
casematch = 0

for w in x.split():
  if(w == y):
    identical = identical + 1
  elif (w.lower() == y.lower()):
    casematch = casematch + 1

if(identical > 0):
 print('found identical matches:', identical)

if(casematch > 0):
 print('found case matches:', casematch)

if(casematch == 0 and identical == 0): 
 print('no matches found')

