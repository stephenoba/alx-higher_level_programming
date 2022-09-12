#!/usr/bin/python3
# 4-list_division.py
# Stephen Oba <obastepheno@gmail.com>

def list_division(my_list_1, my_list_2, list_length):
    """Divide the integers in two lists"""
    new_list = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
