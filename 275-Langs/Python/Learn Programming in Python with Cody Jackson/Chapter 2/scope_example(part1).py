var1 = 1  # global variable

if var1 == 1:
    var2 = 0  # also a global variable
    print("Unmodified var2: {}".format(var2))

def my_funct():
    var3 = 3  # local variable
    var1 = 42  # shadows global var1 variable
    global var2
    var2 = 80 
    print("Inside function, var1: {}".format(var1))
    print("Inside function, var2: {}".format(var2))
    print("Inside function, var3: {}".format(var3))
