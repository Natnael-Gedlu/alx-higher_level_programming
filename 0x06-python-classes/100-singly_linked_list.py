#!/usr/bin/python3
"""
Define classes for a singly-linked list.
"""


class Node:
    """
    This class defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a node with data and an optional next_node.

        :param data: The data to be stored in the node.
        :type data: int
        :param next_node: The next node in the linked list (default is None).
        :type next_node: Node or None
        :raises TypeError: If data is not an integer,
        or if next_node is not a Node or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data stored in the node.

        :return: The data stored in the node.
        :rtype: int
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        :param value: The data value to set.
        :type value: int
        :raises TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node in the linked list.

        :return: The next node in the linked list.
        :rtype: Node or None
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        :param value: The next node value to set.
        :type value: Node or None
        :raises TypeError: If value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list.
    """

    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position
        in the list (increasing order).

        :param value: The value to be inserted into the linked list.
        :type value: int
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the linked list.

        :return: A string representation of the linked list.
        :rtype: str
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()


# Example usage
linked_list = SinglyLinkedList()
linked_list.sorted_insert(5)
linked_list.sorted_insert(2)
linked_list.sorted_insert(8)
print(linked_list)
