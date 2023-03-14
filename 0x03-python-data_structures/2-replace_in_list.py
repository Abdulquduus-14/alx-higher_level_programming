#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """function that replaces an element of a list at a specific point
    Args:
    my_list: list of integers
    idx: position of element to replace
    element: new value to insert

    Return: nothing
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
