import random


choice = "paper"  # Computer chooses paper.
print ("Rock-paper-scissors: type in your choice:    ")
player = input ()
print (random.randint(0,5))

# --------- The new section of code ---------------------
while player == choice:   # Repeat input until there is a winner
    print ("Game is a tie. Please try again.")
    player = input ()
# -------------------------------------------------------

if player == "rock":
    if choice == "scissors":
        print ("Congratulations. You win.")
    else:
        print ("Sorry - computer wins.")
elif player == "paper":
    if choice == "scissors":
        print ("Sorry - computer wins.")
    else:
        print ("Congratulations. You win.")
elif player == "scissors":
    if choice == "rock":
        print ("Sorry - computer wins.")
    else:
        print ("Congratulations. You win.")
else:
    print ("Error: Select one of: rock, paper, scissors")

