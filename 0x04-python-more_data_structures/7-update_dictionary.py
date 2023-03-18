#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    a function that replaces or adds key/value in a dictionary.

    Args:
    a_dictionary: dat structure to work on
    key: argument will be always a string
    value: new value to associate with a key

    Returns: new dictionay
    """
    for k in a_dictionary.keys():
        if k == key:
            a_dictionary[key] = value
    a_dictionary[key] = value
    return a_dictionary
