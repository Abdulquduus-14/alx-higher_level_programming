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
    d = {}
    if key in a_dictionary.key():
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
