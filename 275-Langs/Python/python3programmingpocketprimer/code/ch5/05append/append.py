outfile = open ("out.txt", "a")
for i in range (25, 45):
    sout = "    "+str(i)+"              "+str(i*i)+"\n"
    outfile.write (sout)
outfile.close()