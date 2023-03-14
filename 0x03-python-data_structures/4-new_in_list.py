#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """function that replaces an element in a list at a specific position

    Args:
    my_list: list of integers
    idx: position of integer
    element: new value of element at idx

    Return: new list on success, else old list
    """

    i = 0

    for i in my_list:
        continue
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
