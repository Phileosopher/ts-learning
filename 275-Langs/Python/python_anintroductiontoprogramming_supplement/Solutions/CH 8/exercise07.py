# Exercise 8.07


def printdate (y,m,d,h,min,s):
    print ("{:4d}-{:02d}-{:02d}T{:02d}-{:02d}-{:.1f}".format(y, m, d, h, min,s) )

year=2016
month = 12
day = 6
hour = 11
minute = 21
second = 33.5

printdate(year,month,day,hour, minute, second)