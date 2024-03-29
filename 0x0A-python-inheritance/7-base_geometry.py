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

    def integer_validator(self, name, value):
        """ function that that validates value

        Args:
        name(str): name of geometery
        value(int): size of geometry

        Returns:
        None
        """
        if not(isinstance(value, int)):
            raise TypeError("{} must be an integer".format(self.value))
        if value <= 0:
            msg = "{} must be greater than 0".format(self.value)
            raise ValueError(msg)
        self.name = name
        self.value = value
