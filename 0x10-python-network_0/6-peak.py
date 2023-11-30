#!/usr/bin/python3
"""
Gets the peak from a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
     Gets the peak from the list_of_integers
     """
    if not list_of_integers:
        return None

    lo, hi = 0, len(list_of_integers)

    while lo < hi:
        mid = (lo + hi) // 2

        if (mid == 0 or list_of_integers[mid]
            >= list_of_integers[mid - 1]) and \
                (mid == len(list_of_integers) - 1 or
                 list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    return None
