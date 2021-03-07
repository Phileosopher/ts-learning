import re

line1 = "abc def"
result1 = re.split(r'[\s]', line1)
print('result1:',result1) 

line2 = "abc1,abc2:abc3;abc4"
result2 = re.split(r'[,:;]', line2)
print('result2:',result2) 

line3 = "abc1,abc2:abc3;abc4 123 456"
result3 = re.split(r'[,:;\s]', line3)
print('result3:',result3) 

