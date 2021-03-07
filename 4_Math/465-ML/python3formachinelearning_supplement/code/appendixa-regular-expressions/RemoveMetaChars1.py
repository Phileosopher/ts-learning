import re

text1 = "meta characters ? and / and + and ."
#text2 = re.sub(".*/(?=[^/]+)","",text1)
text2 = re.sub("[/\.*?=+]+","",text1)

print('text1:',text1)
print('text2:',text2)


