#!/usr/bin/python3
def magic_string():
    """
    Generate a magic string with increasing repititions of ""BestSchool.

    The number of repititions is determined by the value of the attribute 'n'
    of the magic_string function. 'n' keeps track of the number of times
    the magic_string function has been called.
    """
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("Bestschool, " * (magic_string.n + 1) + "BestSchool")
