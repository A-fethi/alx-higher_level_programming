#!/usr/bin/python3
def square_matrix_simple(matrix=[[]]):
    result = list(
            map(lambda x: list(map(lambda y: (y**2), x)), matrix)
            )
    return result
