import re

line1 = "abcdef"
line2 = "123,abc1,abc2,abc3"
line3 = "abc1,abc2,123,456f"

if re.match("^[A-Za-z]*$", line1):
  print('line1 contains only letters:',line1)

# better than the preceding snippet:
if line1[:-1].isalpha():
  print('line1 contains only letters:',line1)

if re.match("^[\w]*$", line1):
  print('line1 contains only letters:',line1)

#if re.match(r"^[^\W\d_]+$", line1, re.LOCALE):
#  print('line1 contains only letters:',line1)
#print()

if re.match("^[0-9][0-9][0-9]", line2):
  print('line2 starts with 3 digits:',line2)

if re.match("^\d\d\d", line2):
  print('line2 starts with 3 digits:',line2)
print()

if re.match("[0-9][0-9][0-9][a-z]$", line3):
  print('line3 ends with 3 digits and 1 char:',line3)

if re.match("[a-z]$", line3):
  print('line3 ends with 1 char:',line3)


