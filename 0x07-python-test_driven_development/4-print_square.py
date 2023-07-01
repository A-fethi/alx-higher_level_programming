#!/usr/bin/python3
"""Module of "4-print_square"."""


def print_square(size):
    """
    Prints a square with the chracter #.
    """
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) in [float] and size < 0:
        raise TypeError("size must be an integer")
    i = 0
    while i < size:
        print("#" * size)
        i += 1
