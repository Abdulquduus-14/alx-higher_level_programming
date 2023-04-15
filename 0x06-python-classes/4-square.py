#!/usr/bin/python3
""" an class Square that defines a square with size"""


class Square:
    """ an class Square that defines a square.
    Instantiation with size attribute is done

    Attributes
    size (int): private instance attributes defin
    """

    def size(self, value):
        """ initializes object attributs

        Args:
        size (int): length of square

        Returns:
        nothing
        """
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return the area

        Args: none

        Returns: area of square
        """
        return (self.__size * self.__size)

    def size(self):
        """ getter function
        Args: nothing
        Returns: nothing
        """
        return (self.__size)

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
