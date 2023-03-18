#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    function that computes the square value of all integers of a matrix.
    Args:
    matrix: 2 dimensional array
    Returns: a new matrix of integers
    """
    for [x, y, z] in matrix:
        x *= x
        y *= y
        z *= z
    return matrix
