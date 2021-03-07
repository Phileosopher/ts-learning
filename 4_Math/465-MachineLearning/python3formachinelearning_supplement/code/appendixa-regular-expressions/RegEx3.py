import re

line2 = "abc1,Abc2:def3;Def4"
result2 = re.split(r'[,:;]', line2)

for w in result2:
  if(w.startswith('Abc')):
    print('Word starts with Abc:',w)
  elif(w.endswith('4')):
    print('Word ends with 4:',w)
  else:
    print('Word:',w)
  
