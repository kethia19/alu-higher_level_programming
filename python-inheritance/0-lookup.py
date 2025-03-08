#!/usr/bin/python3

""" Module to lookup all attributes of an object. """


def lookup(obj):
    """ Function to return the list of available attributes of an object. """
    return dir(obj)
