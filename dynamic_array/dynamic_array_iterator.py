from typing import Any, Self

class DynamicArrayIterator:
    """An iterator that traverses the array from 0 through end"""

    def __init__(self, dynamic_array) -> None:
        """Initialize the iterator at the start of the array"""
        self.dynamic_array = dynamic_array
        self.cur_index = 0

    def __iter__(self) -> Self:
        """Return this iterator"""
        return self

    def __next__(self) -> Any:
        """Return the next value in the array
        :raises StopIterator: when end of array is reached"""
        if self.cur_index >= len(self.dynamic_array):
            raise StopIteration
        return_data = self.dynamic_array.get(self.cur_index)
        self.cur_index += 1
        return return_data