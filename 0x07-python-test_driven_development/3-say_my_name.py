#!/usr/bin/python3

""" a function that prints a person's full name """


def say_my_name(first_name, last_name=""):
    """ a function that prints My name is <first name> <last name>

    Args:
    first_name: strings for first name
    last_name: strings for last name

    Returns: Nothing
    """
    if not(isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not(isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
