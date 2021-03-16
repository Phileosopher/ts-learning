# Exercise 5.1  Count bytes in a file
name = input("Enter the name of a file: ")
count = 0
try:
    infile = open(name, "r")
    while True:
        c = infile.read(1)
        if c == "": break
        count = count + 1
        if count%100 == 0: print (count)
    print ("There were ", count, " characters in this file.")
except FileNotFoundError:
    print ("There is no file named ", name)
