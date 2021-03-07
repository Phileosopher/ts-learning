line = '1 2 3 4 10e abc'
sum  = 0
invalidStr = ""

print('String of numbers:',line)

for str in line.split(" "):
  try:
    sum = sum + eval(str)
  except:
    invalidStr = invalidStr + str + ' '

print('sum:', sum)
if(invalidStr != ""):
  print('Invalid strings:',invalidStr)
else:
  print('All substrings are valid numbers')

