#!/usr/bin/python3
""" an class Square that defines a square with size"""


class Square:
    """ an class Square that defines a square.
    Instantiation with size attribute is done

    Attributes
    size (int): private instance attributes defin
    """
    def __init__(self, size=0):
        """ initializes object attributs

        Args:
        size (int): length of square

        Returns:
        nothing
        """
        if not(isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
