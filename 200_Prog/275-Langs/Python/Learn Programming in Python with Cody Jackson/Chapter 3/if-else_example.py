def preference():
    answer = input("What is your favorite room in the house?")
    if answer == "kitchen":
        print("You probably like food.")
    elif answer == "bedroom":
        print("You probably like to sleep.")
    elif answer == "living room":
        print("You probably like to watch TV.")
    else:
        print("Maybe you prefer to be outdoors.")
