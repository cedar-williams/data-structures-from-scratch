from typing import Any

from node import Node
from linked_list_iterator import LinkedListIterator

class LinkedList:
    """Linked list implementation"""

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0


    def push(self, data: Any) -> None:
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

    def insert(self, index: int, data: Any) -> None:
        """Add a new node at the specific index, valid index: 0 <= index <= len(list)
        :raises IndexError: if the index is out of the range of the list"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            if index == 0: # First node
                cur_node = self.head
                self.head = new_node
                new_node.next_node = cur_node
                cur_node.prev_node = new_node
            elif index == self.size: # After last node
                back_node = self.tail
                self.tail = new_node
                back_node.next_node = new_node
                new_node.prev_node = back_node
            else: # In the middle
                cur_node = self._node_at_index(index)
                back_node = cur_node.prev_node
                new_node.prev_node = back_node
                new_node.next_node = cur_node
                back_node.next_node = new_node
                cur_node.prev_node = new_node
        self.size += 1


    # TODO
    def remove(self, index: int) -> Any:
        """Remove node at current index
        :raises IndexError: if the index is out of the range of the list"""
        raise NotImplementedError

    def get(self, index: int) -> Any:
        """:returns: data of node at index
        :raises IndexError: if the index is out of the range of the list"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self._node_at_index(index).data

    def set(self, index: int, data: Any) -> Any:
        """Sets the data value of an existing node at the specified index
        :raises IndexError: if the index is out of the range of the list"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self._node_at_index(index).data = data

    def clear(self) -> None:
        """Empties the list"""
        self.head = None
        self.tail = None
        self.size = 0

    def _node_at_index(self, index: int) -> Node:
        """Index must refer to a valid node
        :returns: Node at index"""
        node_count = 0
        current_node = self.head
        while node_count < index:
            current_node = current_node.next_node
            node_count += 1

        return current_node


    def __len__(self) -> int:
        """:returns: number of nodes in list"""
        return self.size

    def __iter__(self) -> LinkedListIterator:
        """Returns an iterator that traverses the LinkedList from head to tail.
        :returns: An iterator for traversing the linked list"""
        return LinkedListIterator(self)