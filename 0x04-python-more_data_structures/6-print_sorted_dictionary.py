#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ans_1 = list(a_dictionary.keys())
    ans_2 = ans_1.sort()
    for i in ans_1:
        print("{}: {}".format(i, a_dictionary.get(i)))
