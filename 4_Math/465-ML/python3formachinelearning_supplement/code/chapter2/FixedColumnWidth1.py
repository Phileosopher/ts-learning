import string

left = 0
right = 0
columnWidth = 8

str1 = 'this is a string with a set of words in it and it will be split into a fixed column width'
strLen = len(str1)

print('Left-justified column:') 
print('----------------------') 
rowCount = int(strLen/columnWidth)

for i in range(0,rowCount):
   left  = i*columnWidth
   right = (i+1)*columnWidth-1
   word  = str1[left:right]
   print("%-10s" % word)

# check for a 'partial row'
if(rowCount*columnWidth < strLen):
   left  = rowCount*columnWidth-1;
   right = strLen
   word  = str1[left:right]
   print("%-10s" % word)

