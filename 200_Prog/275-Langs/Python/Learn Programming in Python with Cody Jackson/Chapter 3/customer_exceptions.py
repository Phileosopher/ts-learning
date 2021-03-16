import math

class NegativeNumberError(ValueError): 
    """Attempted improper operation on negative number."""
    pass

def squareRoot(number):
    """Computes square root of number. Raises NegativeNumberError if number is less than 0."""
    if number < 0:
        raise NegativeNumberError("Square root of negative number not permitted")
	
    return math.sqrt(number) 

if __name__ == "__main__":
    squareRoot(-3)
