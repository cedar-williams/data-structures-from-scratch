from typing import Any

class StackItem:
    __slots__=("item", "next_down")

    def __init__(self, item, next_down = None):
        self.item = item
        self.next_down = next_down


class Stack:

    def __init__(self) -> None:
        self.top = None

    def empty(self) -> bool:
        """:returns: True is stack is empty, false if populated"""
        return self.top is None

    def peek(self) -> Any:
        """:return: top item of stack without removing it"""
        self._ensure_not_empty()
        return self.top.item

    def push(self, item: Any) -> None:
        """Add item on top of stack"""
        new_item = StackItem(item)
        new_item.next_down = self.top
        self.top = new_item

    def pop(self) -> Any:
        """Return item on top of stack
        :raises IndexError: if stack is empty"""
        self._ensure_not_empty()
        return_node = self.top
        self.top = self.top.next_down
        return return_node.item

    def _ensure_not_empty(self) -> None:
        """:raises IndexError: if stack is empty"""
        if self.top is None:
            raise IndexError("Stack is empty")