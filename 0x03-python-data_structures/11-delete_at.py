#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """ function that deletes the item at a specific position in a list.
    Args:
    my_list: list of integers
    idx: position of element
    Return: nothing
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
