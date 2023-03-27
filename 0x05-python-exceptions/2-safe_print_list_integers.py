#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ function that prints the first x elements of a list.
    Args:
    my_list: list of elements
    x: number of elements to print

    Returns:  the real number of integers printed
    """
    c = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]))
            c += 1
        except (IndexError, ValueError, TypeError):
            print()
        except Exception:
            print()
