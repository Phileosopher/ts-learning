# Jeopardy!
import csv
import random

try:
    infile = open ("JEOPARDY_small.txt", "r")  # Open the file
    reader = csv.reader(infile)   # Make a reader
    s = reader.__next__()         # Read (skip over) the header line

    CORRECT = 0
    INCORRECT = 0
    again = True
    while again:
        k = random.randint (5, 10) # How many questions to skip?
        try:
            for i in range (0, k):
                s = reader.__next__()  # Skip this question
            s = reader.__next__()      # Read the question to be asked.
        except:
            close(infile)
            infile = open ("JEOPARDY_small.txt", "r")
        print (s[5])               # Print the question
        a = input ()               # Read the answer
        if a == s[6]:              # Does player answer agree with the file?
            CORRECT = CORRECT + 1  # Yes. count to 10.
            if CORRECT >= 10:
                print ("You win!")
                again = False
        else:
            INCORRECT = INCORRECT + 1  # No. Count to 3
            print ("Sorry. The answer is ", s[6])
            if INCORRECT > 2:
                print ("You lose.")
                again = False
except FileNotFoundError:
        print ("There is no question file.  We can't play.")

