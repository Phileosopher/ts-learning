    elif choice == 6: #d12 roll
    	die = random.randint(1, 12)
    elif choice == 7: #d20 roll
    	die = random.randint(1, 20)
    else:   #simple error message
        return "Shouldn't be here.  Invalid choice"
    return die

def multiDie(dice_number, die_type):
    """Add die rolls together, e.g. 2d6, 4d10, etc."""
    
#---Initialize variables    
    final_roll = 0
    val = 0
