from typing import Any

import pytest

from dynamic_array import DynamicArray

def make_dynamic_array(length: int) -> DynamicArray:
    new_dynamic_array = DynamicArray()
    for i in range(length):
        new_dynamic_array.append(value_at_index(i))
    return new_dynamic_array

def value_at_index(index: int) -> Any:
    return f"obj {index}"

# Creation
def test_init():
    new_dynamic_array = DynamicArray()
    assert len(new_dynamic_array) == 0
    assert str(new_dynamic_array) == "DynamicArray[ ]"

def test_array():
    new_dynamic_array = make_dynamic_array(3)
    assert len(new_dynamic_array) == 3
    assert str(new_dynamic_array) == "DynamicArray[ obj 0 obj 1 obj 2 ]"

@pytest.mark.parametrize("array_size, comparison_value, expected_result",
                         [(1, "DynamicArray[ ]", False),
                          (1, "obj 0", True)])
def test_contains(array_size, comparison_value, expected_result):
    new_dynamic_array = make_dynamic_array(array_size)
    assert (comparison_value in new_dynamic_array) == expected_result
