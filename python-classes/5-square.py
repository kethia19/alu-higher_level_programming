#!/usr/bin/python3

"""Square Class.

This module contains a class that defines a square.

"""


class Square:
    """This class defines the blueprint of a square."""

    def __init__(self, size=0):
        """
        Initializes Square with size.

        Args:
            size: An integer representing object size.
                  Has a default value of 0.
        """
        self.__size = size

    @property
    def size(self):
        """Gets the size private attribute value.

        Returns:
            The size private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size private attribute value.

        Args:
            value: the value to be set.
        
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """Display the square object with # character."""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
