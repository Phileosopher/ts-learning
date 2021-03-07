import string

wordCount = 0
str1 = 'this is a string with a set of words in it'

print('Left-justified strings:')
print('-----------------------')
for w in str1.split():
   print('%-10s' % w)
   wordCount = wordCount + 1
   if(wordCount % 2 == 0):
      print("")
print("\n")

print('Right-justified strings:') 
print('------------------------') 

wordCount = 0
for w in str1.split():
   print('%10s' % w)
   wordCount = wordCount + 1
   if(wordCount % 2 == 0):
      print()

