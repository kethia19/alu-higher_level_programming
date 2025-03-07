#!/usr/bin/python3

"""Square Class.

This module contains a class that defines a square.
"""


class Square:
    """This class defines the blueprint of a square."""

    def __init__(self, size=0):
        """Initialize square with size.

        Args:
            size: An integer representing object size.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
