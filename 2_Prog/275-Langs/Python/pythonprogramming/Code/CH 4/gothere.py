def gothere (count, value=None):
    if value:
        print ("Got Here: ",count, " value is ", value)
    else:
        print ("Got Here: ", count)

year = 2015
a = year % 19
gothere(1)
b = year // 100
c = year % 100
gothere(2)
d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
gothere(3, f)
month = f // 31
day = f % 31 + 1
gothere(4, day)
print (year, month, day)
