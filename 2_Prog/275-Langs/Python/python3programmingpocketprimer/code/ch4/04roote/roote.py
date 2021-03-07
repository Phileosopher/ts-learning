
def addup (data):
    sum = 0
    for i in range(0,len(data)):
        sum = sum + data[i]
    return sum

data = [1,5,23,12,45,34,89,91]
sum = addup(data)
print ("The list sums to", sum)
