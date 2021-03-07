import random

def displayState():
    print("Display state")

def prompt():	
    print("Enter move")
    
def makeMove():			
    print ("Make move")

def gameOver():
    if random.random()<0.2:
        return False
    return True

def makeComputerMove():		
    print ("compute a move")

def printWinner():
    print("The winner is:")

done = False
while not done:              	# Run until the game is over
    displayState()     	# Show the game board
    prompt()             	# Ask user for their move
    makeMove ()       	# Make it
    if not gameOver():	# Computer move?
        makeComputerMove()# Determine computer’s move
    done = gameOver()		# Is the game over?
printWinner()

