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
    except ZeroDivisionError:
        return "None"
    finally:
        print("{}{}".format("Inside result:", result))
        return result
