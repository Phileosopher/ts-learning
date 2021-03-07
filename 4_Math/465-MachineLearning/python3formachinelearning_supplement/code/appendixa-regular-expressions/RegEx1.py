import re

str1 = "123456"
matches1 = re.findall("(\d+)", str1)
print('matches1:',matches1) 

str1 = "123456"
matches1 = re.findall("(\d\d\d)", str1)
print('matches1:',matches1) 

str1 = "123456"
matches1 = re.findall("(\d\d)", str1)
print('matches1:',matches1) 

print
str2 = "1a2b3c456"
matches2 = re.findall("(\d)", str2)
print('matches2:',matches2) 

print
str2 = "1a2b3c456"
matches2 = re.findall("\d", str2)
print('matches2:',matches2) 

print
str3 = "1a2b3c456"
matches3 = re.findall("(\w)", str3)
print('matches3:',matches3) 

