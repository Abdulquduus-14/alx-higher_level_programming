#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    a function that deletes a key in a dictionary.

    Args:
    a_dictionary: structure to delete from
    key: key to delete


    Returns:
    new dictionary structure
    """
    d = {}
    if key in a_dictionary:
        del a_dictionary[key]
    d = a_dictionary
    return d
