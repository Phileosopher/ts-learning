str1 = "okra is the closest thing to nylon i've ever eaten."
str2 = "pull the string, and it will follow wherever you wish."
str3 = "let out a little more string on your kite."
str4 = "every string is a different color, a different voice."
vowels = 'aeiou'
alph  = 'abcdefghijklmnopqrstuvwxyz'
alph6 = 'ghijklmnopqrstuvwxyzabcdef'

encr = "varr znk yzxotm, gtj oz corr lurruc cnkxkbkx eua coyn."
for i in str1:
    if i in alph:
        j = alph.index(i)
        k=alph6[j]
    else:
        k = i
    print(k, end='')
print ()

for i in encr:
    if i in alph6:
        j = alph.index(i) - 6
        if j<0:
            j = j + len(alph)
        k = alph[j]
    else:
        k = i
    print (k, end="")