#!/usr/bin/python3
import json

"""Defines to_json_string function."""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)."""
    return json.dumps(my_obj)
