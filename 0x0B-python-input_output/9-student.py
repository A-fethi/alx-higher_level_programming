#!/usr/bin/python3
"""Define a class called Student."""


class Student:
    """Class represents Student."""
    def __init__(self, first_name, last_name, age):
        """Initialise the Student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return self.__dict__
