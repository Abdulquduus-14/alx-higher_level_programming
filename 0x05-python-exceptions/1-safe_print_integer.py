#!/usr/bin/python3

def safe_print_integer(value):
    """ function that prints an integer

    Args:
    value: number to print

    Returns:
    True if value has been correctly printed, else false
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
