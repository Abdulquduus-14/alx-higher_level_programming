#!/usr/bin/python3
""" a class Rectangle that defines a rectangle """


class Rectangle:
    """" rectangle class definition

    Attributes:
    width (int): wideness of rectangle
    height (int): tallness of rectangle
    """

    def width(self, value):
        """ object constructor method to initialise
        the attribute

        Args:
        value (int): wideness of the rect
        """
        if type(value) is not Int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.width = value

    def width(self):
        """ object constructor method to initialise
        the attribute

        Args:
        None
        Returns: width of rectangle
        """
        return (self.width)

    def height(self, value):
        """ object constructor method to initialise
        the attribute

        Args:
        value (int): wideness of the rect
        """
        if type(value) is not Int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.height = value

    def height(self):
        """ object constructor method to initialise
        the attribute

        Args:
        None
        Returns: height of rectangle
        """
        return (self.height)
