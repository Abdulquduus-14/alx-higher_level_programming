#!/usr/bin/python3

"""
a function that prints all integers of a list.
Args:
    my_list: list of integers
return: 0 for success
"""


def print_list_integer(my_list=[]):

    for i in my_list:
        print("{:d}".format(i))
