import re

line1 = "This is a line"
line2 = "That is a line"

if re.match("^[Tt]his", line1):
  print('line1 starts with This or this:')
  print(line1)
else:
  print('no match')

if re.match("^This|That", line2):
  print('line2 starts with This or That:')
  print(line2)
else:
  print('no match')

