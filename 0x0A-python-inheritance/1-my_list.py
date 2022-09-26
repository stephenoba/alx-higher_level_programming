#!/usr/bin/python3
# 1-my_list.py
# Stephen Oba <obastepheno@gmail.com>
"""Module provides a custom list implementation
"""


class MyList(list):
    """Class inherits from python list class
    """
    def print_sorted(self):
        """Prints a sorted list

        Args:
            None

        Return:
            None
        """
        self.sort()
        print(self)
