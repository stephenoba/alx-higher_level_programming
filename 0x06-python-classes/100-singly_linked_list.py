#!/usr/bin/python3
# 100-singly_linked_list.py
# Stephen Oba <obastepheno@gmail.com>
"""
Module provides a class for creating a singly linked list
"""


class Node:
    """
    Create a node
    """
    def __init__(self, data, next_node=None):
        """Initialize a node insttance"""
        self.data = data
        self.__next_node = next_node

    @property
    def data(self):
        """get the data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """set the data attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set a next_node attribute"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Create a singly linked list
    """
    def __init__(self):
        """initialize a singly linked list object"""
        self.__head = None

    def sorted_insert(self, value):
        """
        inserts a new Node into the correct sorted position
        in the list (increasing order)

        :param value: data of Node
        """
        new_node = Node(value)
        current_node = self.__head
        if not current_node:
            self.__head = new_node
            return

        if current_node.data >= value:
            self.__head = new_node
            new_node.next_node = current_node
            return

        while current_node.next_node:
            if current_node.next_node.data >= value:
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                return
            current_node = current_node.next_node

        current_node.next_node = new_node

    def __str__(self):
        """
        string representation of list
        """
        linked_list = ""
        current = self.__head
        while current:
            if not current.next_node:
                linked_list += "{}".format(current.data)
                break
            linked_list += "{}\n".format(current.data)
            current = current.next_node
        return linked_list
