#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""

class BaseGeometry:
    """Define attributes and methods for geometric shapes."""

    def area(self):
        """Compute the area.

        Raises:
            Exception: If the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): The name of the attribute.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
