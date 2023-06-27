#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """A class representing an object with size attribute."""

    def __init__(self, size=0):
        """
        Initialize the Square object with a given size.

        Parameters:
            size (int) : The size of the object.
        Raises:
            TypeError: size not int
            ValueError: size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """A public instance to return the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
