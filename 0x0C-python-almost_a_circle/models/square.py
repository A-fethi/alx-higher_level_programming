#!/usr/bin/python3
"""Define Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize new square."""
        self.__width = size
        self.__height = size
        super().__init__(self.__width, self.__height, x, y, id)

    def __str__(self):
        """Returns a string presentation of square object."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
