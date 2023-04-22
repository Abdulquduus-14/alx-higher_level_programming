#!/usr/bin/python3
""" A base class module for other claasees """


class Base:
    """ a class to act as base for other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ object initializer
        Atttr:
        id(int): identifier

        Returns: nothing
        """
        if id is not None:
            id = None
        else:
            Base.__nb_objects += 1
