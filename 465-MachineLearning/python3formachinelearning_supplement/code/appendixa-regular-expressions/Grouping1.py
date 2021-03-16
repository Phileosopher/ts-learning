import re

p1 = re.compile('(ab)*')
print('match1:',p1.match('ababababab').group())
print('span1: ',p1.match('ababababab').span())

p2 = re.compile('(a)b')
m2 = p2.match('ab')
print('match2:',m2.group(0))
print('match3:',m2.group(1))

