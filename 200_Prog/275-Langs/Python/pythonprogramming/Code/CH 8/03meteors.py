# Meteorites

infile = open ("met.txt", "r")
inline = infile.readline()
print ("      Place     Class            Mass   Latitude  Longitude")
while inline !="":
    inlist = inline.split(",")
    mass = float(inlist[4])
    lat =  float(inlist[7])
    long = float(inlist[8])
    print('{:16s} {:14s} {:7.2f}'.format(inlist[0], inlist[3], mass), end="")
    print ('  {:7.2f}     {:7.2f}'.format(lat, long))
    inline = infile.readline()
infile.close()
