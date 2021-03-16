// Game of Nim. Seems to work, computer wins.
val = [5, 7, 9]	  # the game state
done = False	  # Is the game over?
userMove = [-1, -1]
move = [-1, -1]

def displayState(val):
    for j in range(0,3):
        print (j+1, ": ", end="")
        for i in range(0,val[j]):
            print ("| ",end="")
        print("   ", val[j])

def rules():
    print("Rules of the game:")
    print("")

def prompt (move):
    row =    input ("Your move: which row? ")
    sticks = input ("           how many matches?")
    move[0] = int(row)-1
    move[1] = int(sticks)

def makeMove(move, state):
    print ("Player move was row ", move[0]+1, " sticks ", move[1])
    row = move[0]
    sticks = move[1]
    state[row] = state[row]-sticks

def legalMove(move, state):
    row = move[0]
    sticks = move[1]
    if row<0 or row>2:
        return False
    if sticks<=0 or sticks>state[row]:
        return False
    return True

def eval (state):
    return state[0]^state[1]^state[2]

def getComputerMove (move, state):
    for i in range(0, 3):
        for j in range(1, val[i]+1):
            state[i] = state[i] - j;
            if eval(val) == 0:
                move[0] = i
                move[1] = j
                state[i] = state[i] + j;
                return
            state[i] = state[i] + j;

def gameOver (state):
    if state[0]==0 and state[1]==0 and state[2]==0:
        return True
    return False

print ("The game of Nim.")
rules()		              # Print the rules for the game
while not done:	          # Run until the game is over
    displayState(val)     # Show the game board
    prompt(userMove)	          # Ask user for their move
    ok = legalMove (userMove, val)  # Was the player’s move OK?
    while not ok:
        print ("This move is not legal.")
        displayState(val)
        prompt(userMove)	  # Ask user for their move
        ok = legalMove (userMove, val)

    print ("User moves: ", end="")
    makeMove (userMove, val)       # Make it
    if gameOver(val):
        print("You win!")
        break;
    print ("State after your move is ")  # display it.

    getComputerMove (move, val)
    print ("Computer's move: ", end="")
    makeMove (move, val)
    if gameOver(val):
        print("Computer wins!")
        break;
    displayState(val)




