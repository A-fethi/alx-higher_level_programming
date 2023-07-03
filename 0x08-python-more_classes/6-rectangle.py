#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """A class representing a Rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialisze the Rectangle object.

        Parameters:
            width, height (int): of the rectangle.

        Raises:
            TypeError: Parameters are not int.
            ValueError: Parameters are less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A public instance to return the current rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """A public instance to return the current rectangle perimeter."""
        if self.__width and self.__height != 0:
            return ((self.__width * 2) + (self.__height * 2))
        return 0

    def __str__(self):
        """Returns a string representation of a rectangle."""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        i = 0
        while i < self.__height:
            string += "#" * self.__width
            if i < self.__height - 1:
                string += "\n"
            i += 1
        return string

    def __repr__(self):
        """Return a string representation of the object."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
