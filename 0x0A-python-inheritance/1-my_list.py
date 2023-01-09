#!/usr/bin/python3
"""
Defines MyList which is subclass of list,
"""
class MyList(list):
    """
    Inherites from list
    """
    def print_sorted(self):
        """prints the list in ascending order)"""
        print(sorted(self))