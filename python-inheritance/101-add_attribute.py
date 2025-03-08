#!/usr/bin/python3
"""Module that defines a function to add a new attribute to an object."""

def add_attribute(obj, name, value):
    """Add a new attribute to an object.

    Args:
        obj: The object to which the attribute will be added.
        name: The name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
