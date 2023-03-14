#!/usr/bin/python3

def max_integer(my_list=[]):
    """ a function that finds the biggest integer of a list.
    Args:
    my_list: list of integers
    Return:
    maximum value on success, else 0
    """
    max = my_list[0]
    for i in my_list:
        if my_list[i + 1] > my_list[i]:
            max = my_list[i + 1]

        return max
