#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """  a function that checks if the object is exactly an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Args:
    obj(instance of a class): object to verify its class
    a_class(class type): class type of object

    Returns:
    True if the object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class ; otherwise False.
    """
    if not(issubclass(obj, a_class)):
        return False
    else:
        return True
