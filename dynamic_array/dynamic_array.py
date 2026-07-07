from typing import Any, Generic, TypeVar, List
from dynamic_array_iterator import DynamicArrayIterator

class DynamicArray:
    """Dynamic array of generic type"""

    def __init__(self, capacity: int = 10) -> None:
        """Initialize a DynamicArray"""
        self.length = 0
        self.capacity = capacity
        self.list = []

    def append(self, item):
        """Add item to the end of the array"""
        self.list.append(item)
        self.length += 1
        self._update_capacity()

    def get(self, index: int) -> Any:
        """Returns item at specified index
        :raises IndexError: if index is invalid"""
        if index < 0 or index >= self.length:
            raise IndexError("Requested index is outside of array")
        return self.list[index]

    #Capacity changes
    def _update_capacity(self):
        """Change capacity if needed"""
        if self.length == self.capacity:
            self._grow()
        elif (self.length <= self.capacity / 2) and (self.capacity >= 2):
            self._shrink()

    def _grow(self):
        """Increase the capacity of the array"""
        self.capacity *= 2

    def _shrink(self):
        """Decrease the capacity of the array"""
        self.capacity /= 2

    def __eq__(self, other: Any) -> bool:
        """Return true if both DynamicArray's match,false if not."""
        if not isinstance(other, DynamicArray):
            return NotImplemented

        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self.get(i) != other.get(i):
                return False
        return True

    def __len__(self) -> int:
        """:returns: the size of the array"""
        return self.length

    def __iter__(self) -> DynamicArrayIterator:
        """Returns the iterator class, this makes it so multiple iterators can run simultaneously"""
        return DynamicArrayIterator(self)

    def __contains__(self, item:Any) -> bool:
        """:returns: true if item is in array, false otherwise"""
        for i in self:
            if i == item:
                return True
        return False

    def __str__(self) -> str:
        """:returns: String representation of array"""
        string = "DynamicArray[ "
        for item in self:
            string += str(item) + " "
        return string + "]"
