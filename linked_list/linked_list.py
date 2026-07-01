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

    def remove(self, index: int) -> Any:
        """Remove node at current index
        :raises IndexError: if the index is out of the range of the list"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        removed_node = self._node_at_index(index)
        if self.size == 1:
            self.clear()
        else:
            if index == 0: # First node
                self.head = self.head.next_node
                self.head.prev_node = None
            elif index == self.size - 1: # Last node
                self.tail = self.tail.prev_node
                self.tail.next_node = None
            else:
                back_node = removed_node.prev_node
                front_node = removed_node.next_node
                back_node.next_node = front_node
                front_node.prev_node = back_node
            self.size -= 1
        return removed_node.data

    def get(self, index: int) -> Any:
        """:returns: data of node at index
        :raises IndexError: if the index is out of the range of the list"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self._node_at_index(index).data

    def set(self, index: int, data: Any) -> None:
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

    def index(self, data: Any) -> int:
        """:returns: index of first match
        :raises ValueError: if match not found"""
        cur_node = self.head
        index = 0
        if cur_node is None:
            raise ValueError
        while cur_node is not None:
            if cur_node.data == data:
                return index
            index += 1
            cur_node = cur_node.next_node
        raise ValueError

    def reverse(self) -> None:
        """Reverse the LinkedList in place"""
        cur_node = self.head

        # Swap head and tail
        old_head = self.tail
        self.head = self.tail
        self.tail = old_head

        while cur_node is not None: # Swap prev next node
            back_node = cur_node.prev_node
            cur_node.prev_node = cur_node.next_node
            cur_node.next_node = back_node

            cur_node = cur_node.prev_node


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

    def __eq__(self, other: "LinkedList") -> bool:
        """:return NotImplemented: if other is not of same type"""
        if not isinstance(other, LinkedList):
            return NotImplemented
        if len(self) != len(other):
            return False

        my_node = self.head
        other_node = other.head
        while my_node is not None:
            if not my_node.data == other_node.data:
                return False
            else:
                my_node = my_node.next_node
                other_node = other_node.next_node

        return True

    def __contains__(self, item) -> bool:
        """:returns: True if item in list, false if not"""
        for single_item in self:
            if single_item == item:
                return True
        return False

    def __getitem__(self, index: int) -> Any:
        return self.get(index)

    def __setitem__(self, index: int, data: Any) -> None:
        self.set(index, data)

    def __delitem__(self, index: int) -> None:
        self.remove(index)

    def __str__(self):
        return "LinkedList(" +  str(list(self)) + ")"

    def __repr__(self):
        return "LinkedList(" +  str(list(self)) + ")"