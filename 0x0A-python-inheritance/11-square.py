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
