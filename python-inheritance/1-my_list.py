#!/usr/bin/python3
"""Module that provides the MyList class."""

class MyList(list):
    """A subclass of list with an additional method to print a sorted version."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
