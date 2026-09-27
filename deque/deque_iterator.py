from typing import Self, Any


class DequeIterator:
    """An iterator that traverses the deque from top to bottom."""

    def __init__(self, deque) -> None:
        """Initialize an iterator at the top of the deque
        :param deque: the deque to iterate over"""
        self.current_node = deque.tail

    def __iter__(self) -> Self:
        """:return: this iterator"""
        return self

    def __next__(self) -> Any:
        """Return the next value in the deque
        :raises StopIteration: when there are no more list items
        :returns: data in next node"""
        if self.current_node is None:
            raise StopIteration

        data = self.current_node.val
        self.current_node = self.current_node.prev
        return data