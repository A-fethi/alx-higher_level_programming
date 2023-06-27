#!/usr/bin/python3
"""Define a MagicClass class"""
import math


class MagicClass:
    """A class representing an object with radius attribute."""
    def __init__(self, radius=0):
        """Initialize the MagicClass object with a given radius."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """A public instance to return the multuplication."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """A public instance to return the multiplication."""
        return 2 * math.pi * self.__radius
