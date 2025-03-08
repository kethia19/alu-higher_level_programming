#!/usr/bin/python3
"""Module that provides the lookup function."""

def lookup(obj):
    """Return a list of available attributes and methods of an object.
    
    Args:
        obj: The object to inspect.
    
    Returns:
        list: A list of attribute and method names.
    """
    return dir(obj)
