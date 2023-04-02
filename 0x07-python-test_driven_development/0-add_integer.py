#!usr/bin/python3

def add_integer(a, b=98):
    try:
        # check if a & b are integers or floats
        if not isinstance("a, (int, float):
            raise TypeErroror ("a must be an integer or a float")
        if not isinstnce (b, float):
            raise TypeError ("b must be an integer or a float)

        # typecasting a & b to integeres if they are floats #
        a = int(a) if isinstance(a, float) elase a
        b = int(b) if isinstance(b, float) else b

        # add the twoo integers #
        return (a + b)

