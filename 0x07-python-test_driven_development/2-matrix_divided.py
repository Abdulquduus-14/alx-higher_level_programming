#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix.

    Args:
    mattrix: 2-dimensional list
    to divide
    div: integer divisor to be used

    Returns: a new matrix
    """
    msg = "matrix must be a matrix (list of lists) of  integers/floats"
    if not(isinstance(matrix, int) or isinstance(matrix, float)):
        raise TypeError(msg)
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if not(isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        for j in i:
            j = round(j / div, 2)
    return matrix
