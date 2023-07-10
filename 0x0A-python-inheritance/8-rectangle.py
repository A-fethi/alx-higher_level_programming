#!/usr/bin/python3
"""Define BaseGeometry class."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry."""
    def __init__(self, width, height):
        """instantation of the rectangle."""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
