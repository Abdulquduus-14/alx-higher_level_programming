#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """ prints all integers of a list, in reverse order.
    Args:
    my_list: list of integers
    Return:
    nothing
    """

    for i in my_list[-1:]:
        print("{:d}".format(i))
