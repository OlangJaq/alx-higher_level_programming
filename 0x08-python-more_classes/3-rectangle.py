#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """
    This class defines a rectangle with a given width and height.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        The constructor for the Rectangle class.

        Args:
            width (int): The initial width of the rectangle.
            height (int): The initial height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The new width value for the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The new height value for the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public instance method to calculate the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Public instance method to calculate the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'.

        Returns:
            A string representation of the rectangle using '#'.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for i in range(self.height):
            rect_str += "#" * self.width
            if i != self.height - 1:
                rect_str += "\n"
        return rect_str
