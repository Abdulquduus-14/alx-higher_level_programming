#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """function that replaces an element of a list at a specific point
    Args:
    my_list: list of integers
    idx: position of element to replace
    element: new value to insert

    Return: nothing
    """
    i = 0

    for i in my_list:
        i += i
    while i >= 0:
        if i == idx:
            my_list[idx] = element
            i -= 1
