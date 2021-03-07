import random #randint

def randomNumGen(choice):
    """Get a random number to simulate a d6, d10, or d100 roll."""
    
    if choice == 1: #d6 roll
    	die = random.randint(1, 6)
    elif choice == 2: #d10 roll
        die = random.randint(1, 10)
    elif choice == 3: #d100 roll
        die = random.randint(1, 100)
    elif choice == 4: #d4 roll
    	die = random.randint(1, 4)
    elif choice == 5: #d8 roll
    	die = random.randint(1, 8)  
