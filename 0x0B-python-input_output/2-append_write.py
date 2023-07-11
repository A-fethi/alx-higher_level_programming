#!/usr/bin/python3
"""Defines append_write function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a  text file
    and returns the nb of chars added."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
