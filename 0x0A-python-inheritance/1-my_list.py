#!/usr/bin/python3
"""
Defines a class MyList that inherits from list.
"""

class MyList(list):
    def print_sorted(self):
        """
        Print the elements of the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        for item in sorted_list:
            print(item, end=" ")
