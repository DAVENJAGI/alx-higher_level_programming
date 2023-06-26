#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_0 = []
    for n in range(0, list_length):
        try:
            div = my_list_1[n] / my_list_2[n]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            list_0.append(div)
    return (list_0)
