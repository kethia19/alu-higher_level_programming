#!/usr/bin/python3


"""Module that provides the is_kind_of_class function."""

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or its subclass.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)

