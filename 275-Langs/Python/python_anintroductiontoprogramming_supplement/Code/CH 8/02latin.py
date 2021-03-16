def load_words (name, dict):  # Read the file of words
    f = open (name, "r")
    s = f.readline()          # Read one word pair
    while s != "":            # exit when the file has been read
        c = s.split (",")     # Split at the comma
        if len(c)<2:          # Possible error: no words?
            s = f.readline()  # Read next and continue
            continue
        sw = c[0].strip()     # Get the latin and English words.
        ew = c[1].strip()
        if len(ew) <=0:       # OK?
            s = f.readline()  # Nope. Just skip it.
            continue
        if ew[-1] == "\n":    # Get ride of the endline
            ew = ew[0:-2]
        dict[sw] = ew         # Place in dictionary
        s = f.readline()      # Next word pair from the file
    f.close()                 # Always close when done

dict = {}
load_words("latin.txt", dict)  # Read all of the word pairs

inp = input("Enter a latin phrase ") # Get the Latin text
while inp != "":                     # Done?
    book = inp.split(" ")            # Split at words
    for i in range(0,len(book)):     # For each word this line
        sword = book[i].lower()      # Lower case
        try:
            enword = dict[sword]    # Look up Latin word
            print (enword, end="")  # Print English version
        except:
            print (sword, end="")   # Latin not in dictionary
        print (" ", end="")         # Print the Latin
    print (".")
    inp = input("Enter a latin phrase ") # Do it again
