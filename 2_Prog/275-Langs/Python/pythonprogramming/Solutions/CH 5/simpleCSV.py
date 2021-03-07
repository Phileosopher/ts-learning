# simpleCSV module.
# Basic reading of a CSV file. No class.

__record = ""      # The record being examined.

def trim (s):      # Remove spaces from the beginning of the string s
    i = 0
    while s[i] == ' ':  # Look at characters one at a time. Space?
        i = i + 1       # index i increases until non-space is seen
        if i>=len(s):   # End of string? They were ALL spaces
            return ""
    return s[i:]        # On loop end i is index of non-space

def eatcomma (s):  # Skip characters until a comma is seen
    if s == "": return ""
    i = 0               # Start at the first character in s
    while s[i] != ',':  # Is this a comma?
        i = i + 1       # No. Increment index to look at the next character
        if i>=len(s):   # Emd of string? No comma then
            return ""
    return s[i+1:]      # At end of loop, i is index of the comma.

def nextRecord (file):  # Read the next record from the file
    global __record
    __record = file.readline()
    if len(__record) > 0: return True
    return False

def strParse (s):  # Look for a string - ignore commas within
    c = s[0]            # C is the delimiter, either ' or "
    i = 1               # First character in the string has index 1
    while i < len(s):   # Scan characters looking for delimiter
        if s[i] == c:   # Found it!
            return i    # Return index of closing quote
        i = i + 1       # Otherwise keep looking
    return i-1          # Not found, no closing quote

def fparse (s):  # Look for a field - terminated by comma
    i = 0               # First character has index 0
    while i < len(s):   # Scan consecutive chars looking for comma
        if s[i]==',':   # Found a comma!
            return i    # Return the index of the comma
        i = i + 1       # Otherwise keep looking
    return i            # Not found. Could be end of line.

def getData (file): # Parse the current string into fields
    global __record
    ret = ()            # Return a tuple
    i = 0               # Start at the first character in __record
    s = __record
    while (len(s)>0):   # So long as there are characters left ...
        s = trim(s)     # Remove leading spaces
        if s[i] == '"' or s[i] == "'":       # A string
            k = strParse(s)                  # Locate it
            ff = s[1:k]                      # Make a copy
            s = s[k+1:]                      # Remove from input
            s = eatcomma(s)                  # Comma?
        #    field = "'" + ff + "'"           # Add to output
            field = ff           
        else:                              # Not a string
            k = fparse(s)                  # Parse field
            field = s[:k]                  # Make a copy
            s = s[k:]                      # Remove from input
            if s != "": s = eatcomma(s)    # Comma?
        ret = ret + (field,)           # Build tuple by concatenation
    return ret


#try:
#    infile = open("JEOPARDY_small.txt", "r")
#except FileNotFoundError:
#    print ("No such file")
#    exit()

#nextRecord (infile)
#print ("Record 1 is ", __record)
#x = getData (infile)
#print (x)

#for i in range(0,100):
#    nextRecord(infile)
#    print ("Record ", i+2, " is ", __record)
#    x = getData (infile)
#    print (x)
