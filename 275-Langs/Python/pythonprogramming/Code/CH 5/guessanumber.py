choice = 7
guessed = False
while not guessed:
    print ("Please guess a number between 1 and 10: ")
    try:
        playerchoice = int(input())
        guessed = True
    except:
        print ("Sorry, your guess must be an integer.")
    if playerchoice<10 or playerchoice>10:
        print ("Your guess was ", playerchoice, " which is out of range.")
        guessed = False
if choice == playerchoice:
    print ("You win!")
else:
    print ("Sorry, you lose.")