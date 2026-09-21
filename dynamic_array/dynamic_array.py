from typing import Any, Generic, TypeVar, List
from dynamic_array_iterator import DynamicArrayIterator

class DynamicArray:
    """Dynamic array of generic type"""

    # Percent of capacity size should be at when grow or shrink is triggered
    CAPACITY_RATIO_GROW_THRESHOLD = 1
    CAPACITY_RATIO_SHRINK_THRESHOLD = 0.25

    MINIMUM_CAPACITY = 1

    def __init__(self, capacity: int = MINIMUM_CAPACITY) -> None:
        """Initialize a DynamicArray"""
        self.length = 0
        self.capacity = capacity
        self.list = [None] * self.capacity

    def append(self, item: Any) -> None:
        """Add item to the end of the array"""
        self._update_capacity()
        self.list[self.length] = item
        self.length += 1

    def insert(self, index: int, item: Any) -> None:
        """Insert item at specified index"""
        self.length += 1
        self._update_capacity()
        cur_item = self.get(index)
        self.list[index] = item

        for x in range(index + 1, self.length):
            tmp = self.list[x]
            self.list[x] = cur_item
            cur_item = tmp

    def remove(self, index) -> Any:
        """Remove and return item at index"""
        item = self.list[index]
        for x in range(index, self.length - 1):
            self.list[x] = self.list[x + 1]

        self.length -= 1
        self._update_capacity()
        return item

    def get(self, index: int) -> Any:
        """Returns item at specified index
        :raises IndexError: if index is invalid"""
        if index < 0 or index >= self.length:
            raise IndexError("Requested index is outside of array")
        return self.list[index]

    def set(self, index: int, item: Any) -> None:
        """Set the value of the item at the specified index"""
        self.list[index] = item

    def clear(self) -> None:
        """Empty the array"""
        self.length = 0
        self._update_capacity()

    # Capacity changes
    def _update_capacity(self) -> None:
        """Change capacity if needed"""
        cur_cap_ratio = self._capacity_size_ratio()
        if cur_cap_ratio >= self.CAPACITY_RATIO_GROW_THRESHOLD:
            self._grow()
        elif ((cur_cap_ratio < self.CAPACITY_RATIO_SHRINK_THRESHOLD) and
              (self.capacity > self.MINIMUM_CAPACITY)):
            self._shrink()

    def _grow(self) -> None:
        """Increase the capacity of the array"""
        self.capacity *= 2
        for x in range(self.length, self.capacity):
            self.list.append(None)

    def _shrink(self) -> None:
        """Decrease the capacity of the array"""
        self.capacity /= 2

    def _capacity_size_ratio(self) -> float:
        """Return a ratio of how full the array is"""
        return self.length / self.capacity

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

    def __getitem__(self, item: int) -> Any:
        return self.get(item)

    def __setitem__(self, index, item) -> None:
        self.list[index] = item