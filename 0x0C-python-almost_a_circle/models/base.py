#!usr/bin/python3
"""the base class of all other classes"""


class Base:
    """
    Represents the base for all classes in the project oxoc*
    Attributes:
        __nb__objects (int): The number of instantiated bases.
    """

    
    __nb__objects = 0
    # class constructor
    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of thr new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects