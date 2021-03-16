# Game of Sticks. More or less works.
val = 21        # The game state, initially 21 sticks
done = False	  # Is the game over?
userMove = 0
move = 0

# Display the game at this point.
def displayState(val):
    k = val
    while k > 0:
        if k >=6:
            for j in range(0,6):
                print ("O ", end="")
            k = k - 6
        else:
            for j in range(0,k):
                print ("O ", end="")
            k = 0
        print ("")

def rules():
    print("Rules of the game:")
    print ("  (1) There are two players. Label them You and Computer.")
    print ("  (2) There is a pile of 21 chips in the center of a table.")
    print ("  (3) A move consists of removing one, two, or three chips from the pile. At least one")
    print ("      chip must be removed, but no more than three may be removed.")
    print ("  (4) Players alternate moves with You starting.")
    print ("  (5) The player that removes the last chip wins. (The last player to move wins. If you")
    print ("      can’t move, you lose.")
    print("")

def prompt ():
     n = int(input ("Your move: Take away how many?  "))
     while n<=0 or n>3:
        print ("Sorry, you must take 1, 2, or 3 sticks.")
        n = int(input ("Your move: Take away how many?  "))
     return n


def makeMove(move):
    global val
    if move <= val:
        val = val - move
        print ("You took ", move, " sticks leaving ", val)

def legalMove(move, val):
    if move<= val:
        return True
    return False

def getComputerMove (val):
    n = val % 4
    if n<=0:
        return 1
    else:
        return n

def gameOver (state):
    if val == 0:
        return True
    return False

print ("The game of Sticks.")
rules()		              # Print the rules for the game
while not done:	          # Run until the game is over
    displayState(val)     # Show the game board

    userMove = prompt()	          # Ask user for their move
    ok = legalMove (userMove, val)  # Was the player’s move OK?
    while not ok:
        print ("This move is not legal.")
        userMove = prompt()	  # Ask user for their move
        ok = legalMove (userMove, val)
    print ("User moves: ", userMove)
    if userMove <= val:
        val = val - userMove
    print ("You took ", userMove, " sticks leaving ", val)
    if gameOver(val):
        print("You win!")
        break;

    move = getComputerMove (val)
    print ("Computer's move: ", move)
    if move <= val:
        val = val - move
    print ("Computer took ", move, " sticks leaving ", val)
    if gameOver(val):
        print("Computer wins!")
        break;
    displayState(val)

