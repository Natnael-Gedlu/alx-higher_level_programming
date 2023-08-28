#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for element in my_list:
            if i < x:
                print(element, end=' ')
                i += 1
        print()
    except:
        pass

    return i
