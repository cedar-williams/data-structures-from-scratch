from typing import Any

from node import Node

class LinkedList:
    """Linked list implementation"""

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data) -> None:
        """Add a new node at end of list
        :param data: the value or object to be added to the LinkedList"""
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            node.prev_node = self.tail
            self.tail = node

        self.size += 1

    def pop(self) -> Any:
        """Remove the last node from the list
        :return: Data of node, None if list is empty
        :raises IndexError: if the list is empty"""
        if self.head is None:
            raise IndexError("List is empty")
        else:
            self.size -= 1
            return_data = self.tail.data
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail.prev_node.next_node = None
                self.tail = self.tail.prev_node

            return return_data

    def __len__(self) -> int:
        """:returns: number of nodes in list"""
        return self.size