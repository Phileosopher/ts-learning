# 5.5 - Read CSV file, create new file for level 10.
import simpleCSV

infile = open ("avatardata.csv", "r")
outfile = open("level10.csv", "w")
while True:
    if simpleCSV.nextRecord(infile):
        data = simpleCSV.getData(infile)
        level = int(data[3])
        if level == 10:
            outfile.write(data[0])
            outfile.write(",  ")
            outfile.write(data[1])
            outfile.write(",  ")
            outfile.write(data[2])
            outfile.write(",  ")
            outfile.write (data[3])
            outfile.write(",  ")
            outfile.write(data[4])  # Newline is part of data[4]!
        #    outfile.write("\n")  # Otherwise we'd have to do this.
    else:
        break
infile.close()
outfile.close()