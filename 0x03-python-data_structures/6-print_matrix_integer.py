#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """ a function that prints a matrix of integers.
    Args:
    matrix: arrray of integers
    Return:
    nothing
    """

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print("{:d}".format(matrix[i][j]), end=" ")
            print()
