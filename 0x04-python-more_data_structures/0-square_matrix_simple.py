#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    function that computes the square value of all integers of a matrix.
    Args:
    matrix: 2 dimensional array
    Returns: a new matrix of integers
    """
    m = [][]
    for i in range(3):
        for j in range(3):
            m[i][j] = matrix[i][j] ** 2

    return m
