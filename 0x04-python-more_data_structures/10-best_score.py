#!/usr/bin/python3


# best_score - Function that returns key with biggest int value
def best_score(my_dict):
    if my_dict is None or my_dict == {}:
        return None
    biggest = max(my_dict.values())
    for key, value in my_dict.items():
        if value is biggest:
            return key