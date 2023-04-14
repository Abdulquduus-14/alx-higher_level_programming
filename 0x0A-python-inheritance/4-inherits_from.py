#!/usr/bin/python3
"""  a function that checks if the object is exactly an
instance of the specified class or its derived class """


def inherits_from(obj, a_class):
    """  a function that checks if the object is exactly an
    instance of the specified class or its derived class

    Args:
    obj(instance of a class): object to verify its class
    a_class(class type): class type of object

    Returns:
    True if the object is exactly an instance of the specified class;
    otherwise False.
    """
    isinstance(obj, a_class)
