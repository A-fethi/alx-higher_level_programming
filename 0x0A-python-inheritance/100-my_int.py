#!/usr/bin/python3
"""Defines MyInt class."""


class MyInt(int):
    """Inverts operators"""
    def __ne__(self, value):
        """Override != to =="""
        return self.real == value

    def __eq__(self, value):
        """Override == to !="""
        return self.real != value
