
text1 = 'a b c d'
text2 = 'a b c e d'

if(text2.find(text1) >= 0):
  print('text1 is a substring of text2')
else:
  print('text1 is not a substring of text2')

subStr = True
for w in text1.split():
  if(text2.find(w) == -1):
    subStr = False
    break

if(subStr == True):
  print('Every word in text1 is a word in text2')
else:
  print('Not every word in text1 is a word in text2')

