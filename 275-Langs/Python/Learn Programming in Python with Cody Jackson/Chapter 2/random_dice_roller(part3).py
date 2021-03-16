    while val < dice_number:
        final_roll += randomNumGen(die_type)
        val += 1
    return final_roll
       
if __name__ == "__main__":  #run test() if calling as a separate program
    """Test criteria to show script works."""
    
    _1d6 = multiDie(1,1)   #1d6
    print("1d6 = ", _1d6, end=' ')    
    _2d6 = multiDie(2,1)   #2d6
    print("\n2d6 = ", _2d6, end=' ')
    _3d6 = multiDie(3,1)   #3d6
    print("\n3d6 = ", _3d6, end=' ')
