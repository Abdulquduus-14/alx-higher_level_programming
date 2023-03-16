#!/usr/bin/python3

def number_keys(a_dictionary):
    """
    a function that returns the number of keys in a dictionary.

    Args:
    a_dictionary: a dictionary data structure to count elements

    Returns:
    number of keys in dictionary
    """
    c = 0
    for k in a_dictionary.keys():
        c += 1

    return c
