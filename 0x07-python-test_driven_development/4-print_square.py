#!/usr/bin/python3
""" Printing a square shape using '#' """


def print_square(size):
    """ a function that prints a square

    Args:
    size: length of square to prints

    Returns: nothing
    """
    if not(isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
