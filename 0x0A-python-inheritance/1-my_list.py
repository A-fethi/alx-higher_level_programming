#!/usr/bin/python3
"""Define inherited MyList class."""


class MyList(list):
    """Sorted printing implementation."""
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
