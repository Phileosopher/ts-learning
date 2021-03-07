import re

line1 = "this is a line of text"
print('line1:',line1) 

# Matching Words
#"\S+"          # as many non-whitespace bytes as possible
#"[A-Za-z'-]+"  # as many letters, apostrophes, and hyphens

# string split is similar to splitting on "\s+"
line2 = "A text   with some\tseparator".split()
print('line2:',line2)

print("A text   with some\tseparator".split())
print("A text   with some\tseparator".split("\S+"))

words1 = re.match("\b*([A-Za-z]+)\b*", line1)   # word boundaries 
words2 = re.match("\s*([A-Za-z]+)\s*", line1)   # might work too as on letters are allowed.

#print(words1)
#print(words2)

word3 = re.search("\Bis\B","this thistle") # matches on thistle not on this
word4 = re.search("\Bis\B","vis-a-vis")    # does not match

#print(word3)
#print(word4)

