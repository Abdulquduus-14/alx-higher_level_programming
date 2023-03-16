#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    a function that adds all unique integers in a list

    Args:
    my_list: liust of integers
    Returns:
    sum of list of integers
    """
    s = set(my_list)
    sum = 0
    for x in s:
        sum += x
    return sum
