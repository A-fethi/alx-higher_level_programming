#!/usr/bin/python3
"""Define Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new rectangle."""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
