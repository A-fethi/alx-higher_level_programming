#!/usr/bin/python3
"""Defines save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
