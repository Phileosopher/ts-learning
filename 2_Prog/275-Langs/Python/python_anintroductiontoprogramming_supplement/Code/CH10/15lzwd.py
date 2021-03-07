
s = ""
ch = ""
dict = []
count = 0
for i in ('A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ', ',', '.'):
    dict = dict + [i,]
    count = count + 1

s = ""
inf = open ("lzwtext.txt", "r")
code1 = int(inf.readline())        # CODE1 is the first code on the file
print (dict[code1], end="")        # Output the string for CODE1
while True:                        # While mode codes on the file ...
    c = inf.readline()
    if c == '':
        break
    code0 = int(c)                # CODE0 is the next code on the file
    if code0 < len(dict):         # Is CODE0 in the table?
        s = dict[code0]           # YES. S is the string for CODE0
    else:
        s = dict[code1]           # NO. S is the string for CODE1
        s = s + ch                # Append CH to S.
    print (s, end="")             # IN EITHER CASE emit S
    ch = s[0]                     # CH becomes the first character of S
    dict = dict + [dict[code1]+ch,]
    count = count + 1
    code1 = code0
print()
