#!/usr/bin/python3
""" an empty class BaseGeometry with raised unimplemented
area method exception """


class BaseGeometry:
    """ future class representation """
    def area(self):
        """ area of geometry
        Args: none
        Returns: None
        """
        raise Exception("area() is not implemented")
