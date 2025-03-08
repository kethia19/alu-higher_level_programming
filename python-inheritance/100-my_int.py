#!/usr/bin/python3
"""Module that defines the MyInt class, a subclass of int with inverted equality behavior."""

class MyInt(int):
    """Define a custom integer class with inverted equality and inequality operators."""

    def __eq__(self, other):
        """Return the result of != check instead of ==."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Return the result of == check instead of !=."""
        return int.__eq__(self, other)
