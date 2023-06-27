#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """A class representing an object with size attribute."""

    def __init__(self, size=0, position=(0, 0)):
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
        self.size = size
        self.position = position

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

    def my_print(self):
        """A public instance to print the square in stdout with # character."""
        if self.__size == 0:
            print()
        elif self.__position[1] > 0:
            i = 0
            while i < self.__position[1]:
                print()
                i += 1
            i = 0
            while i < self.__size:
                print(" " * self.__position[0] + "#" * self.__size)
                i += 1
        else:
            i = 0
            while i < self.__size:
                print(" " * self.__position[0] + "#" * self.__size)
                i += 1

    @property
    def position(self):
        """Retrieve the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position attribute."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
