from typing import Any

from deque_iterator import DequeIterator


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

    def append(self, val: Any) -> None:
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

    def append_left(self, val: Any) -> None:
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
        if self.tail is self.head:
            tmp_node = self.tail
            self.tail = None
            self.head = None
            self.length = 0
            return tmp_node.val
        else:
            tmp_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return tmp_node.val

    def pop_left(self) -> Any|None:
        """Pop val at bottom of queue and return it
        :return: the list item"""
        if self.head is None:
            return None
        if self.tail is self.head:
            tmp_node = self.tail
            self.tail = None
            self.head = None
            self.length = 0
            return tmp_node.val
        else:
            tmp_node = self.head
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return tmp_node.val

    def peek(self) -> Any|None:
        """:return: value at top of queue, None if empty"""
        if self.tail:
            return self.tail.val
        else:
            return None

    def peek_left(self) -> Any|None:
        """:return: value at bottom of queue, None if empty"""
        if self.head:
            return self.head.val
        else:
            return None

    def clear(self) -> None:
        """Empty the queue"""
        self.head = None
        self.tail = None
        self.length = 0

    def size(self) -> int:
        """:return: size of queue"""
        return self.__len__()

    def reverse(self) -> None:
        """Reverse the list in place"""
        old_head = self.head
        old_tail  = self.tail
        cur = self.head
        while cur is not None:
            next_node = cur.next
            tmp = cur.prev
            cur.prev = next_node
            cur.next = tmp
            cur = next_node
        self.head = old_tail
        self.tail = old_head

    def __contains__(self, item):
        """:return: True if item in deque, else false"""
        cur = self.head
        while cur is not None:
            if cur.val == item:
                return True
            cur = cur.next

        return False

    def __len__(self) -> int:
        """:return: number of items in queue"""
        return self.length

    def __bool__(self) -> bool:
        """:return: True if list has items"""
        return self.length > 0

    def __str__(self) -> str:
        """:return: string representation of deque"""
        return self.__repr__()

    def __repr__(self) -> str:
        """:return: reproducible string of deque"""
        out_str = self.__class__.__name__ + "[ "
        cur = self.tail
        while cur:
            out_str += cur.val + " "
            cur = cur.prev
        out_str += "]"
        return out_str

    def __eq__(self, value: object, /) -> bool:
        """:return: True if match, false otherwise"""
        if not isinstance(value, Deque):
            return NotImplemented

        if len(self) != len(value):
            return False

        cur_s = self.head
        cur_v = value.head
        while cur_s:
            if cur_s.val != cur_v.val:
                return False
            cur_s = cur_s.next
            cur_v = cur_v.next

        return True

    def __iter__(self):
        """Returns an iterator that traverses the deque from head to tail,
        :return: An iterator for traversing the deque"""
        return DequeIterator(self)