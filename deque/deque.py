from typing import Any


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    """Queue/deque implementation"""
    def __init__(self):
        self.head = None # Front/top
        self.tail = None
        self.length = 0

    def append(self, val) -> None:
        """Add val to top of queue
        :param val: the list item
        """
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def append_left(self, val) -> None:
        """Add val to bottom of queue
        :param val: the list item
        """
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop(self) -> Any|None:
        """Pop val at top of queue and return it
        :return: The list item"""
        if self.tail is None:
            return None
        else:
            tmp_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return tmp_node

    def pop_left(self):
        """Pop val at bottom of queue and return it
        :return: the list item"""
        if self.head is None:
            return None
        else:
            tmp_node = self.head
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return tmp_node

    def peek(self):
        """:return: value at top of queue, None if empty"""
        if self.tail:
            return self.tail.val
        else:
            return None

    def peek_left(self):
        """:return: value at bottom of queue, None if empty"""
        if self.head:
            return self.head.val
        else:
            return None

    def __len__(self):
        """:return: number of items in queue"""
        return self.length

    def __bool__(self):
        """:return: True if list has items"""
        return self.length > 0