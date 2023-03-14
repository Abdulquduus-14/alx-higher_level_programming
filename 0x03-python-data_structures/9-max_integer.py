#!/usr/bin/python3

def max_integer(my_list=[]):
    """ a function that finds the biggest integer of a list.
    Args:
    my_list: list of integers
    Return:
    maximum value on success, else 0
    """
    max = my_list[0]
    if len(my_list) == 0:
        return 'None'
    for i in range(len(my_list)):
        if my_list[i + 1] > my_list[i]:
            max = my_list[i + 1]

        return max
