#!/usr/bin/python3
try:
        def safe_print_list(my_list=[], x=0):
                my_list = [1,2,3]
                for y in my_list:
                        x+=1
                        print(x)
except:
        print("error occurred")
