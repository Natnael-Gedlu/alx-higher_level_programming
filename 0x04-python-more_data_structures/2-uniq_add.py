#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_sum = 0
    unique_elements = set()

    for num in my_list:
        if num not in unique_elements:
            unique_sum += num
            unique_elements.add(num)

    return unique_sum
