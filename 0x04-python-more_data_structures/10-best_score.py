#!/usr/bin/python3

def best_score(a_dictionary):
    """
    a function that returns a key with the biggest integer value.

    Args:
    a_dictionary
    Returns:
    the biggest integer value.
    """

    for v in a_dictionary.values():
        max = v
    for v in a_dictionary.values():
        if v > max:
            max = v
    return max
