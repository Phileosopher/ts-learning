from random import *

roll = list(range(0,13))
for i in range(1,13):
    roll[i] = set()

for i in range (1,7):
    for j in range (1,7):
        k = i+j
        roll[k].add( (i,j) )

winner = roll[7] | roll[11]
loser = roll[2] | roll[3] | roll[12]

die1 = randrange(1,7)
die2 = randrange(1,7)
val = (die1,die2)
print ("Shooter rolls ", val)
if val in winner:
    print ("The shooter wins!")
elif val in loser:
    print ("The shooter loses")
else:
    point = roll[die1+die2]
    print (die1+die2, " is your point.")
    while True:
        die1 = randrange(1,7)
        die2 = randrange(1,7)
        val = (die1, die2)
        print ("Rolls ", val)
        if val in roll[7]:
            print ("The shooter loses!")
            break
        if val in point:
            print ("The shooter makes the point. A winner!")
            break