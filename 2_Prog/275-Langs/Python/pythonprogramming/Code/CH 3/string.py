statement = 'print ("Lcase < numbers")'
print (statement)
print (statement[0:5])
print (statement[:5])
print (statement[6:])
str = "if "+statement[6:]+":"
print (str)
city = "Denver"
k = len(city)
for i in range(0,len(city)):
    city = city + city[k-i-1]
city = city[len(city)//2:]
print (city)
str = "This string has 30 characters."
print (str[::-1])
for c in str:
    print (c)