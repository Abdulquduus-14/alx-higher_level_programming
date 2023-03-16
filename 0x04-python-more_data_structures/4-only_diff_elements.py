#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    computes a set of all elements present in only one set
    from two different sets

    Args:
    set_1: first set of integers
    set_2: second set of integers

    Returns:
    a newly formed set
    """
    s = set()
    s = set_1 ^ set_2
    return s
