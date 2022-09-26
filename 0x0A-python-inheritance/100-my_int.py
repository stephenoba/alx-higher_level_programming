#!/usr/bin/python3
# 100-my_int.py
# Stephen Oba <obastepheno@gmail.com>
""""Module contains MyInt class
"""


class MyInt(int):
    """Representation of a rabel int
    """
    def __eq__(self, other):
        """Implement not equal ;)

        Args:
            other (Any): other type to be compared with

        Return:
            True or False
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Implement equal ;)

        Args:
            other (Any): other type to be compared with

        Return:
            True or False
        """
        return super().__eq__(other)
