#!/usr/bin/python3
"""Define BaseGeometry class."""


class BaseGeometry:
    """Base Geometry."""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) not in [int]:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
