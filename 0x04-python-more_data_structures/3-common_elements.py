#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    a function that returns a set of common elements in two sets.

    Args:
    set_1: first set of integers
    set_2: second set of integers

    Returns:
    intersection of set_1 and set_2
    """
    s = set()
    s = set_1 & set_2
    return s
