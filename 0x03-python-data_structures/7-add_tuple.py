#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """ a function that adds 2 tuples.
    Args:
    tuple_a: first list
    tuple_b: second list

    Return: new tuple
    """
    n = ()
    for i in range(2):
        n[i] = tuple_a[i] + tuple_b[i]
    return n
