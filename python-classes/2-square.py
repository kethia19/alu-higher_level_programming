#!/usr/bin/python3

"""Square Class.

This module contains a class that defines a square.

"""


class Square:
    """This class defines the blueprint of a square."""

    def __init__(self, size=0):
        """Initialize square with size.

        Args:
            size: A integer representing object size.

        Raises:
            TypeError: if size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
