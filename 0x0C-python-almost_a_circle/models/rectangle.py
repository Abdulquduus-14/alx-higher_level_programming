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


class Rectangle(Base):
    """ derived class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor
        Attr:
        width(int): breadth of rect
        height(int): tallness of rect
        x(int): distance from x-coordinate
        y(int): distance from y-coordinate
        Returns: nothing
        """
        Base.__init__(self, id=None)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def x(self):
        return self.__X
    def(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    @width.setter
    def width(self, width):
        self.__width = width

    @height.setter
    def x(self, height):
        self.__height = height
