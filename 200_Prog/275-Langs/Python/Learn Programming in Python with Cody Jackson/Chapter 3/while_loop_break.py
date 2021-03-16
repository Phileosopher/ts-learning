x = 50
while x:
    x -= 1
    if x % 2 != 0:
        continue
    print(x)
    if x == 10:
        break
