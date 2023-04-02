#!usr/bin/python3

def add_integer(a, b=98):
    """function that adds 2 integers."""
    try:
        # Check if a and b are integers or floats
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer or a float")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer or a float")

        # Cast a and b to integers if they are floats
        a = int(a) if isinstance(a, float) else a
        b = int(b) if isinstance(b, float) else b

        # Add the integers and return the result
        return a + b
    
    except TypeError as error:
        print("TypeError:", error)
