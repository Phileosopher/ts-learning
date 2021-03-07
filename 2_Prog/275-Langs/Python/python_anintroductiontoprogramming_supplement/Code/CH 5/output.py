outfile = open ("out.txt", "w")
outfile.write ("    X            X squared \n")
for i in range (0, 25):
#    sout = "    "+str(i)+"              "+str(i*i)+"\n"
    outfile.write ("    ")
    outfile.write (str(i))
    outfile.write ("              ")
    outfile.write (str(i*i))
    outfile.write ("\n")
#    outfile.write (sout)
outfile.close()