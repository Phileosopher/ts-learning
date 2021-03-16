import re

charCount  = 0
digitCount = 0
otherCount = 0

line1 = "A line with numbers: 12 345"

for ch in line1:
   if(re.match(r'\d', ch)):
     digitCount = digitCount + 1
   elif(re.match(r'\w', ch)):
     charCount = charCount + 1
   else:
     otherCount = otherCount + 1

print('charcount:',charCount)
print('digitcount:',digitCount)
print('othercount:',otherCount)

