# Exercise 8.09
# Data file words.txt is this chapter in text form
def letter (c):
    if c>='a' and c<='z':
        return True
    else:
        return False

# Take a string and create a tuple of the words in it
def get_words(s):
    t = ()
    if s == "":
        return t
    ss = s.lower()
    i = 0
    while True:
        if i>=len(ss):
            break
        if not letter(ss[i]):
            i = i + 1
            continue
        j = i
        while letter(ss[j]):
            j = j + 1
        t = t + (ss[i:j],)
        i = j+1
    return t

f = open ("words.txt", "r")    # Input text file
dict = {}                      # Initial dictionary is empty
while True:                    # Until all words have been read
    s = f.readline()           # Read a line of text
    if s == "":                # Done?
        break                  # Yes
    t = get_words(s)           # Extract words from the string

    for word in t:             # Take each word ...
        if word in dict:     #   Look it up . Is it there?
            dict[word] = dict[word] + 1  # Add to the count
        else:
            dict[word] = 1     # If not there, put it there

concordance = sorted(dict.items())
for item in concordance:
    print (item)
