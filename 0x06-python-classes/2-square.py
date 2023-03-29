#!/usr/bin/python3

class Square:
    """ an class Square that defines a square.
    Instantiation with size attribute is done

    Attributes
    siz(int): private instance attributes defin
    """
    def __init__(self, size=0):
        """ initializes object attributs

        Args:
        size (int): length of square

        Returns:
        nothing
        """
        if size < 0:
            raise ValueError("size must be an integer")
        try:
            self.size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
