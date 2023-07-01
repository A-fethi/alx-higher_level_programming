#!/usr/bin/python3
"""Module of "2-matrix_divided"."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for rows in matrix:
        if len(rows) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(message)
            else:
                new_row.append(round(i / div, 2))
        new_matrix.append(new_row)
    return new_matrix
