from typing import Any, Self

class LinkedListIterator:
    """An iterator that traverses the LinkedList from head to tail."""

    def __init__(self, linked_list) -> None:
        """Initialize an iterator at the head of a linked list.
        :param linked_list: The linked list to iterate over"""
        self.current_node = linked_list.head

    def __iter__(self) -> Self:
        """Return this iterator"""
        return self

    def __next__(self) -> Any:
        """Return the next value in the linked list
        :raises StopIteration: If there are no more nodes
        :returns: data stored in next node"""
        if self.current_node is None:
            raise StopIteration
        data = self.current_node.data
        self.current_node = self.current_node.next_node
        return data