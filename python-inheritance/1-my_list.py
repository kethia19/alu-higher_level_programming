#!/usr/bin/python3

""" Module for MyList class that inherits from list. """


class MyList(list):
    """ Class that inherits from the built-in list. """
    def print_sorted(self):
        """ Method that prints the list sorted in ascending order. """
        print(sorted(self))
