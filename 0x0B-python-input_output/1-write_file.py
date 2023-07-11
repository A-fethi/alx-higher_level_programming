#!/usr/bin/python3
"""Defines write_file function."""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the nb of chars."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
