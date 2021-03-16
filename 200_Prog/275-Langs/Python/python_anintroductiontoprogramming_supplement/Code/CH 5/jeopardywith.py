# Jeopardy!
import simpleCSV, random

try:
    with open ("questions.txt") as infile:
        simpleCSV.nextRecord(infile)         # Read (skip over) the header line

        CORRECT = 0
        INCORRECT = 0
        again = True
        while again:
            k = random.randint (5, 10) # How many questions to skip?
            for i in range (0, k):
                if not simpleCSV.nextRecord(infile):   # Skip this question
                    print ("Reopening")
                    infile.seek(0)
                    simpleCSV.nextRecord(infile)
                simpleCSV.nextRecord(infile)
            s = simpleCSV.getData(infile)      # Read the question to be asked.
            print (s[5])               # Print the question
            a = input ()               # Read the answer
            if a.lower() == s[6].lower(): # Does player answer agree with the file?
                CORRECT = CORRECT + 1  # Yes. count to 10.
                if CORRECT >= 10:
                    print ("You win!")
                    again = False
            else:
                INCORRECT = INCORRECT + 1  # No. Count to 3
                print ("Sorry. The answer is ", s[6], " yours was '", a, "'")
                if INCORRECT > 12:
                    print ("You lose.")
                    again = False
except FileNotFoundError:
    print ("There is no question file.  We can't play.")
