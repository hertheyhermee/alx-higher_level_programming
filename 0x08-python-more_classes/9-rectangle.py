#!/usr/bin/python3
"""Defines a class of Rectangle."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        instances (int): The number of Rectangle instances.
        symbol_print (any): The symbol used for string representation.
    """

    instances = 0
    symbol_print = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rectangle_1, rectangle_2):
        """Return the Rectangle with the greater area.

        Args:
            rectangle_1: First Rectangle.
            rectangle_2: Second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rectangle_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rectangle_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rectangle_1.area() >= rectangle_2.area():
            return (rectangle_1)
        return (rectangle_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.

        Args:
            size: Width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.symbol_print)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).instances -= 1
        print("Bye rectangle...")
