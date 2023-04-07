#!/usr/bin/python3
""" a class Rectangle that defines a rectangle """


class Rectangle:
    """" rectangle class definition

    Attributes:
    width (int): wideness of rectangle
    height (int): tallness of rectangle
    """

    @width.setter
    def width(self, value):
        """ object constructor method to initialise
        the attribute

        Args:
        value (int): wideness of the rect
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def width(self):
        """ object constructor method to initialise
        the attribute

        Args:
        None
        Returns: width of rectangle
        """
        return self.__width

    @height.setter
    def height(self, value):
        """ object constructor method to initialise
        the attribute

        Args:
        value (int): wideness of the rect
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def height(self):
        """ object constructor method to initialise
        the attribute

        Args:
        None
        Returns: height of rectangle
        """
        return self.__height
