#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    replaces all occurrences of an element by another in a new list

    Args:
    my_list: string to work with
    search: the element to replace in the list
    replace: the new element

    Returns: new string formed
    """
    for i in my_list:
        if i == search:
            i = replace

    return my_list
