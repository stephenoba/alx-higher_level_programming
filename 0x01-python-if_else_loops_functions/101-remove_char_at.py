#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for i in range(len(str)):
        if i is n:
            continue
        new_str += str[i]
    return new_str