names = []
s = input("Enter a name:")
while  s != 'quit':
    if s in names:
        names.remove(s)
    else:
        names = names + [s]
    print (names)
    s = input("Enter a name:")
