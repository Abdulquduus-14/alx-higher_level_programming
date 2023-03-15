#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """ a function that adds 2 tuples.
    Args:
    tuple_a: first list
    tuple_b: second list

    Return: new tuple
    """
    n = []
    if len(tuple_a) > 2 or len(tuple_b) > 2:
        tuple_a = tuple_a[0:2]
        tuple_b = tuple_b[0:2]
    for i in range(2):
        for(x, y) in zip(list(tuple_a), list(tuple_b)):
            n[i] = x + y
    return tuple(n)
