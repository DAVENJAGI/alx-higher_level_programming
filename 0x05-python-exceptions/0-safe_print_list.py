#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print x elements of a list.
    Args:
        my_list (list): The list to print element from.
        x(int): Number of elements of my list to print.
    Return:
        Number of items in a list.
        """
ret = 0
for i in range(x):
    try:
        print("{}".format(my_list[i]), end="")
        ret += 1
    except IndexError:
        break
    print("")
    return (ret)
