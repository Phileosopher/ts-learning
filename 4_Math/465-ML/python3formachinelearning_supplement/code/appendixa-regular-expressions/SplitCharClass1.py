import re

line1 = '1. Section one 2. Section two 3. Section three'
line2 = '11. Section eleven 12. Section twelve 13. Section thirteen'

print(re.split(r'\d+\. ', line1))
print(re.split(r'\d+\. ', line2))

