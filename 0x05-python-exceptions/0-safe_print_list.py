#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        y = 0
        while y < x:
            print(my_list[y], end="")
            y = y + 1
        print("")
    except IndexError:
        print("")
