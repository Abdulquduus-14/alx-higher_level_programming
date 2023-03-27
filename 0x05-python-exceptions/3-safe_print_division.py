#!/usr/bin/python3

def safe_print_division(a, b):
    """ function that divides 2 integers and prints the result.

    Args:
    a: first integer
    b: second integer

    Returns: the value of the division, otherwise: None
    """
    try:
        result = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        result = None
    finally:
        print("Inside result: {:d}".format(result))
        return (result)
