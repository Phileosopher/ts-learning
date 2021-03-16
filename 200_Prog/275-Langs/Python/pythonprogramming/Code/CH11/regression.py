# Linear regression
from math import *

def mean (x):
    sum = 0.0
    for i in range (0, len(x)):
        sum = sum + x[i]
    sum = sum/len(x)
    return sum

def sdev (x, meanx):
    sum = 0
    for i in range(0,len(x)):
        sum = sum + (x[i]-meanx)*(x[i]-meanx)
    sum = sum/(len(x)-1)
    return sqrt (sum)

def correlate (x, y, meanx, meany):
    sum1 = 0
    sumx2 = 0
    sumy2 = 0
    for i in range(0,len(x)):
        z = (x[i]-meanx)*(y[i]-meany)
        sum1 = sum1 + z
        sumx2 = sumx2 + (x[i]-meanx)*(x[i]-meanx)
        sumy2 = sumy2 + (y[i]-meany)*(y[i]-meany)
    return sum1/sqrt(sumx2*sumy2)

def regress (x, y):
    mx = mean(xdata)
    my = mean(ydata)
    sdx = sdev (xdata, mx)
    sdy = sdev (ydata, my)
    if sdx == 0: return
    r = correlate (xdata, ydata, mx, my)
    m = r * sdy/sdx
    b = my - m * mx
    return (m, b)

def err (x, y, m, b):
    sum = 0
    for i in range (0, len(x)):
        sum = sum + m*x[i]+b-y[i]
    return sum

f = open ("treedata.txt", "r")
s = f.readline ()
xdata = ()
ydata = ()

while s != "":
    for i in range (1,len(s)):
        if s[i] == ",":
            break
    x = float(s[0:i-1])
    y = float(s[i+1:])
    xdata = xdata + (x,)
    ydata = ydata + (y,)
    s = f.readline()

line = regress(x, y)
print ("Equation is y = ", line[0], "*x + ", line[1])
print ("Error is ", err(xdata,ydata, line[0], line[1]))


