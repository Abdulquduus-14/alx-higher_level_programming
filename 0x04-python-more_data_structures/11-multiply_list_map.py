#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    multplies a list by a number without using any loops.

    Args:
    matrix: list of integers
    number: value to multiply list with

    Returns: a new list of integers
    """
    result = list(map(lambda x: x * number, my_list))
    return result
