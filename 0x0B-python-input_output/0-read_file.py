#!usr/bin/python3
"""
Defines a function that reads a text file and prints it to stdout:
"""


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            print(line, end='')
