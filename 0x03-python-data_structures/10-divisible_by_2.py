#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """ a function that finds all multiples of 2 in a list.
    Args:
    my_list: list of integers
    Return: a new list on success, else old list
    """
    new_list = []
    if len(my_list) == 0:
        return [[]]
    else:
        for i in range(len(my_list)):
            if my_list[i] % 2 != 0:
                new_list[i] = False
            else:
                new_list[i] = True
        return new_list
