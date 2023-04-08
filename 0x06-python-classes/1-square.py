#!/usr/bin/python3
""" an class Square that defines a square with size"""


class Square:
    """ an class Square that defines a square.
    Instantiation with size attribute is done

    Attributes
    size (int): private instance attributes defin
    """
    def __init__(self, size):
        """ initializes object attributs

        Args:
        size (int): length of square

        Returns:
        nothing
        """
        self.__size = size
