#!/USR/BIN/PYTHON3
# 9-multiply_by_2.py

def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for i in new_dictionary.keys():
        new_dictionary[i]*=2
    return new_dictionary
