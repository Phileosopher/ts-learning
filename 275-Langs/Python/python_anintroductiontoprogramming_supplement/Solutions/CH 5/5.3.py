# Exercise 5.3  File copy
name = input("Enter the name of a file: ")
count = 0
try:
    infile = open(name, "r")
    name = name[0:-4]+"-copy"+name[-4:]
    print ("Copying to ", name)
    outfile = open (name, "w")
    while True:
        try:
            m = infile.read(1)
            if m == "": break
            outfile.write (m)
        except:
            print ("File error!")
    infile.close()
    outfile.close()
except FileNotFoundError:
    print ("There is no file named ", name)