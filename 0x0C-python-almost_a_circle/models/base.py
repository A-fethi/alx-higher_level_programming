#!/usr/bin/python3
"""Define Base class model."""
import json


class Base:
    """Base model will be the “base” of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation."""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)
