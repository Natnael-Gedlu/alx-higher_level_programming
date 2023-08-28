#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                value_1 = my_list_1[i]
                value_2 = my_list_2[i]
                if (isinstance(value_1, (int, float)) and
                        isinstance(value_2, (int, float))):
                    if value_2 != 0:
                        result.append(value_1 / value_2)
                    else:
                        result.append(0)
                        print("division by 0")
                else:
                    result.append(0)
                    print("wrong type")
            except IndexError:
                result.append(0)
                print("out of range")
    except ZeroDivisionError:
        pass
    finally:
        return result
