#!/usr/bin/env python3

def no_c(my_string):
    """a function that removes all characters c and C from a string.
    Args:
    my_string: array of characters
    return: nothing
    """

    for ch in my_string:
        if ch == 'c' or ch == 'C':
            ch = ''
        s += ch

    return s
