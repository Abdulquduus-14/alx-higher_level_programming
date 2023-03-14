#!/usr/bin/python3

"""
function that retrieves an element from a list like in C.
Args:
    my_list: list of integers
    idx: position of element to retrieve

Return:
    index on success, else None
"""
def element_at(my_list, idx):
    if idx < 0:
        return 'None'
    elif idx > 5:
        return 'None'
    else:
        return my_list[idx]
