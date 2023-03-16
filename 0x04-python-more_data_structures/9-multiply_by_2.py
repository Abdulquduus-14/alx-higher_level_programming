#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    a function that returns a new dictionary with all values multiplied by 2

    Args:
    a_dictionary: structure to work on

    returns: new dictionary
    """
    for v in a_dictionary.values():
        v *= 2

    return a_dictionary
