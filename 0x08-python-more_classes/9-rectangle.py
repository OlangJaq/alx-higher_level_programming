class Rectangle:
    """A class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Return a string representation of the rectangle"""

        if self.width == 0 or self.height == 0:
            return ""
        else:
            return ((str(self.print_symbol) * self.width) + '\n') * self.height

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used to create a new instance
        """

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when the rectangle instance is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """Calculate the area of the rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    @property
    def width(self):
        """Getter for the width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for the height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the biggest area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size"""

        return cls(size, size)
