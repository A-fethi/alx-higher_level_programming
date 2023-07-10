#!/usr/bin/python3
"""Define BaseGeometry class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent the square."""
    def __init__(self, size):
        """Initialize the square."""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns the following rectangle description:
        [Square] <width>/<height>
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
