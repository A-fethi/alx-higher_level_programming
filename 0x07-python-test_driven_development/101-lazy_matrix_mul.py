#!/usr/bin/python3
"""Module of "101-lazy_matrix_mul"."""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices by using the module NumPy.
    """
    return np.dot(m_a, m_b)
