#!/usr/bin/python3
"""Define is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class.
    """
    if isinstance(obj, a_class):
        return True
    return False
