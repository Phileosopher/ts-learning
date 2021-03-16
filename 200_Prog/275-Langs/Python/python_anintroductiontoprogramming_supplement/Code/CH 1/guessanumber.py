# This program selects a number between 1 and
# 10 and allows a user (player) to guess what
# it is.
import random

fail = True
while fail:
# Prompt the user, indicating what we expect
    print ("Please guess a number between 1 and 10: ")
    choice = random.randint(1, 10)   # The number selected by the computer
    print ("Computer selects ",choice)
# Read the player’s input from the keyboard
    playerchoice = int(input())

    # Print the outcome of the game.
    if choice == playerchoice:  # Is the player’s guess
        print ("You win!")      # correct? Player wins!
        fail = False
    else:                 # Otherwise the computer wins
        print ("Sorry, You lose.")
