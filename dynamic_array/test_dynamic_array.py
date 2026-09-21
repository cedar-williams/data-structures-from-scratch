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

def test_capacity_changes():
    new_dynamic_array = DynamicArray(1)
    new_dynamic_array.append(value_at_index(0))
    new_dynamic_array.append(value_at_index(1))
    new_dynamic_array.append(value_at_index(2))
    assert len(new_dynamic_array) == 3
    assert str(new_dynamic_array) == "DynamicArray[ obj 0 obj 1 obj 2 ]"

def test_insert():
    new_dynamic_array = make_dynamic_array(3)
    new_dynamic_array.insert(1, "cat")
    assert str(new_dynamic_array) == "DynamicArray[ obj 0 cat obj 1 obj 2 ]"

def test_get_at_index():
    new_dynamic_array = make_dynamic_array(3)
    assert new_dynamic_array[1] == value_at_index(1)

def test_remove_at_index():
    length = 3
    new_dynamic_array = make_dynamic_array(length)
    assert new_dynamic_array.remove(1) == value_at_index(1)
    assert str(new_dynamic_array) == "DynamicArray[ obj 0 obj 2 ]"
    assert len(new_dynamic_array) == length - 1

def test_set():
    new_dynamic_array = make_dynamic_array(3)
    new_dynamic_array.set(1, "cat")
    assert str(new_dynamic_array) == "DynamicArray[ obj 0 cat obj 2 ]"

def test_eq():
    new_dynamic_array1 = make_dynamic_array(3)
    new_dynamic_array2 = make_dynamic_array(3)
    assert new_dynamic_array1 == new_dynamic_array2

def test_not_eq_by_len():
    new_dynamic_array1 = make_dynamic_array(3)
    new_dynamic_array2 = make_dynamic_array(4)
    assert new_dynamic_array1 != new_dynamic_array2

def test_not_eq_by_content():
    new_dynamic_array1 = make_dynamic_array(3)
    new_dynamic_array2 = make_dynamic_array(3)
    new_dynamic_array2.set(2, "dogs")
    assert new_dynamic_array1 != new_dynamic_array2

def test_contains():
    new_dynamic_array1 = make_dynamic_array(3)
    assert value_at_index(1) in new_dynamic_array1

def test_not_contains():
    new_dynamic_array1 = make_dynamic_array(3)
    assert value_at_index(4) not in new_dynamic_array1

def test_clear():
    new_dynamic_array1 = make_dynamic_array(3)
    new_dynamic_array1.clear()
    assert new_dynamic_array1.length == 0
    assert str(new_dynamic_array1) == "DynamicArray[ ]"