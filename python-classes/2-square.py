#!/usr/bin/python3

"""Square Class.

This module contains a class that defines a square.

"""


class Square:
    """This class defines the blueprint of a square."""

    def __init__(self, size):
        """Initialize square with size.

        Args:
            size: A integer representing object size.

        Raises:
            TypeError: if size is not an integer.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  #: size of the square
