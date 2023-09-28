#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    left = 0
    right = len(list_of_integers) - 1
    loi = list_of_integers
    while left < right:
        middle = (left + right) // 2
        if loi[middle] > loi[middle - 1] & loi[middle] > loi[middle + 1]:
            return loi[middle]
        elif loi[middle] < loi[middle + 1]:
            left = middle + 1
        else:
            right = middle
    return loi[left]
