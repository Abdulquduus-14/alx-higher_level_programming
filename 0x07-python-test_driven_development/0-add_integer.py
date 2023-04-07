#!/usr/bin/python3

def add_integer(a, b=98):
    """ a function that adds 2 integers

    Args:
    a: first integer
    b: second integer

    Returns: the sum of integers a and b
    """
    if type(a) not int or type(b) not int:
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a)
    b = int(b)

    return (a + b)
