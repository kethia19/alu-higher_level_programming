#!/usr/bin/python3
"""Module that defines the Square class, a subclass of Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a square using the Rectangle class."""

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Return the area of the square."""
        return super().area()
