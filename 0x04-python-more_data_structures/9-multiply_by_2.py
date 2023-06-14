#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ans = a_dictionary.copy()
    update = list(ans.keys())
    for n in update:
        ans[n] *= 2
    return(ans)
