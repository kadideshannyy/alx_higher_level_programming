#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    weight = 0
    den = 0
    for x, y in my_list:
        weight += x * y
        den += y
    return (weight / den)