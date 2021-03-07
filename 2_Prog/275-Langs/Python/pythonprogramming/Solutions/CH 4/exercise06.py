# Exercise 4.6


def inputfloat(s):
    try:
        result = input (s)
        return float(result)
    except:
        return None


# Sample test
for i in range (0,10):
    z = inputfloat("Enter a number:")
    if z is None:
        print ("Error: Must be a floating point number")
    else:
        print ("The number was ", z)

