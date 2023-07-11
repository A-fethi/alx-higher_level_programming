#!/usr/bin/python3
"""Defines read_file function."""


def read_file(filename=""):
    """Reads the contents of a file and prints it to the stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
