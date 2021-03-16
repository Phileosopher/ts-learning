tokens = ("False", "class", "finally", "is", "return",
          "None", "continue", "for", 	"lambda", "try",
          "True",	"def",	"from",	"nonlocal",	"while",
          "and",	"del",	"global",	"not",	"with",
          "as", "elif",	"if",	"or",	"yield",
          "assert",	"else",	"import",	"pass",
          "break","except",	"in",	"raise")

def simple (s, size):
        sum = 0
        for i in range (0, len(s)):
            sum = sum + ord(s[i])
        sum = sum%size
        return sum

def djb2 (s, size):
        sum = 5381
        for i in range (0, len(s)):
            sum = sum*33 + ord(s[i])
        sum = sum%size
        return sum

def djbx (s, size):
        sum = 5381
        for i in range (0, len(s)):
            sum = sum*33 ^ ord(s[i])
        sum = sum%size
        return sum

def sdbm (s, size):
    hash = 0
    for i in range (0, len(s)):
        hash = ord(s[i]) * 65599 + hash
    return hash%size

dict = {}
count = 0
for size in range (33, 200):
    count = 0
    dict = {}
    for s in tokens:
        sum = simple (s, size)
        if sum in dict.keys():
            print ("Collision ", dict[sum], s)
        else:
            dict[sum] = s
            count = count + 1
    print (dict)
    print (count)
    if count >= 32:
        print ("------------ ", size ," -----------------------")
        break
    if "False" in dict:
        print ("False")


# DJB2
dict = {}
count = 0
for size in range (33, 200):
    count = 0
    dict = {}
    for s in tokens:
        sum = sdbm(s, size)
        if sum in dict.keys():
            print ("Collision ", dict[sum], s)
        else:
            dict[sum] = s
            count = count + 1
    print (dict)
    print (count)
    if count >= 32:
        print ("------------ ", size ," -----------------------")
        exit()
    if "False" in dict:
        print ("False")
