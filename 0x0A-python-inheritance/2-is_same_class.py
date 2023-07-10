#!/usr/bin/python3
"""Define is_same_class function."""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly a given class's instance
    """
    if type(obj) in [a_class]:
        return True
    return False
