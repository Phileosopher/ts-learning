s = "abc"
print('id #1:', id(s))
print('first char:', s[0])

try: 
  s[0] = "o"
except:
  print('Cannot perform reassignment')

s = "xyz"
print('id #2:',id(s))
s += "uvw"
print('id #3:',id(s))

