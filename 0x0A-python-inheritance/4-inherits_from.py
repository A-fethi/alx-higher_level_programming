#!/usr/bin/python3
"""Define inherits_from function."""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    """
    if isinstance(obj, a_class) and type(obj) not in [a_class]:
        return True
    return False
