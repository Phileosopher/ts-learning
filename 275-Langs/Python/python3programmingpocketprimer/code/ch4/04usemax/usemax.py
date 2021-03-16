import csv

try:
    infile = open ("K:/introProgramming/chapter05/JEOPARDY_small.txt", "r")
except  OSError:
    print ("There is no file named ‘JEOPARDY_small.txt’.  Please try again")
          # end program or abort this section of code

s = infile.readline()  # Skip the header
reader = csv.reader(infile)
row = next(reader)
print (row)
print ("Date: ", row[1])
print ("Question: ", row[5])
print ("Answer: ", row[6])
row = next(reader)
print (row)
if len(row)>1:
    exit()
#print ("0  ", xs[0])
#print ("1  ", xs[1])
#print ("2  ", xs[2])
#print ("3  ", xs[3])
#print ("4   ", xs[4])
for i in range(1,12):
    s = infile.readline()
    xs = s.split(",\"")
    date = xs[0].split(",")[1]
    category = xs[1]
    value = xs[2]
    question = xs[3]
    answer = xs[4]
    print ("Jeopardy question from ", date, " category: ", xs[3], " value ", xs[4])
    print ("What is ", answer)
    print()





