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

    @property
    def width(self):
        """the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        i = 0
        while i < self.__y:
            print()
            i += 1

        j = 0
        while j < self.__height:
            print(" " * self.__x + "#" * self.__width)
            j += 1

    def __str__(self):
        """Returns a string presentation of rectangle object."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle."""
        Dict = {}
        Dict = dict({'x': self.x, 'y': self.y, 'id': self.id,
                    'height': self.__height, 'width': self.__width})
        return Dict
