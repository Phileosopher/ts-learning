# LZW encode

def case(c):
    x = c
    print ("Case ", c, " is ", end="")
    if c>='a' and c<='z':
        x = c.upper()
        print (x)
        return x
    print(c)
    return c

s = ""
ch = ""
dict = {}
count = 0
for i in ('A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ', ',', '.'):
    dict[i] = count
    count = count + 1


inf = open ("data.txt", "r")
ch = case(inf.read(1))
print (ch)
outf = open ("lzwtext.txt", "w")
while len(ch) > 0:
    if s+ch in dict:
        s = s + ch
    else:
        print (dict[s]," ",  end="")
        print (dict[s], file=outf)
        dict[s+ch] = count
        count = count + 1
        s = ch
    ch = case(inf.read(1))
    while ch == '\n':
        ch = case(inf.read(1))
    print(ch)
print (dict[s], file=outf)


# Print the dictionary in order of code value
for j in range(0,len(dict)):
    for k, v in dict.items():
        if v == j:
            print (k, v)
            break