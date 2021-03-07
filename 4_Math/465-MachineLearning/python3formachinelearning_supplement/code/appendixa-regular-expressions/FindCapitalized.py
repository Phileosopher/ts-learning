import re

str = "This Sentence contains Capitalized words"
caps = re.findall(r'[A-Z][\w\.-]+', str) 
 
print('str: ',str)
print('caps:',caps)

