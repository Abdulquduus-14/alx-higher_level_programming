#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    a function that prints a dictionary by ordered keys.

    Args:
    a_dictionary: structure to work with

    Returns:
    """
    d = {}
    d = sorted(a_dictionary)

    for k, v in d.items():
        print("{}: {}".format(k, v))
