import numpy
import pandas

myarray = numpy.array([[10,30,20], [50,40,60],[1000,2000,3000]])

rownames = ['apples', 'oranges', 'beer']
colnames = ['January', 'February', 'March']

mydf = pandas.DataFrame(myarray, index=rownames, columns=colnames)

print(mydf)
print(mydf.describe())

