#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ function that prints x elements of a list
    Args:
    my_list: list of elements to print
    x: the number of elements to print

    Returns: the real number of elements printed
    """
    c = 0

    try:
        for i in range(x):
            print("{:d}".int(format(my_list[i])), end="")
            c += 1
    except (IndexError, ValueError, TypeError, NameError):
        print()

    return c
