from hmac import new

import pytest
import random

from stack import Stack


def make_stack(num_items: int) -> Stack:
    new_stack = Stack()
    # Keeps the output matching the in
    for i in range(1, num_items + 1):
        new_stack.push(f"item {i}")
    return new_stack

def stack_item_at(item_num: int) -> str:
    return f"item {item_num}"


# Test init
def test_init():
    new_stack = Stack()
    assert new_stack.top is None


# Empty
def test_empty_on_empty_stack():
    new_stack = Stack()
    assert new_stack.empty() is True

@pytest.mark.parametrize("num_stack_items", [1,2,10,100])
def test_empty_on_stack_with_items(num_stack_items):
    new_stack = make_stack(num_stack_items)
    assert new_stack.empty() is False


# Peek
def test_peek_on_empty_stack():
    new_stack = Stack()
    with pytest.raises(IndexError):
        new_stack.peek()

@pytest.mark.parametrize("num_stack_items", [1,2,3,4,5,10,20,100])
def test_peek_on_stack_with_items(num_stack_items):
    new_stack = make_stack(num_stack_items)
    assert new_stack.peek() == stack_item_at(num_stack_items)


# Pop
def test_pop_on_empty_stack():
    new_stack = Stack()
    with pytest.raises(IndexError):
        new_stack.pop()

def test_pop_on_stack_with_one_item():
    new_stack = make_stack(1)
    popped_value = new_stack.pop()
    assert popped_value == stack_item_at(1)
    with pytest.raises(IndexError):
        new_stack.peek()

@pytest.mark.parametrize("num_stack_items", [2,3,4,5,10,20,100])
def test_pop_on_stack_with_multiple_items(num_stack_items):
    new_stack = make_stack(num_stack_items)
    popped_value = new_stack.pop()
    assert popped_value == stack_item_at(num_stack_items)
    assert new_stack.peek() != stack_item_at(num_stack_items)


# Search
def test_search_on_empty_stack():
    new_stack = Stack()
    assert new_stack.search("any value") == -1

def test_search_success_two_item_stack_bottom_item():
    new_stack = Stack()
    new_stack.push("item 2")
    new_stack.push("item 1")
    assert new_stack.search("item 2") == 1

@pytest.mark.parametrize("stack_items, search_str, expected_return",
                         [(["item 1"], "item 1", 0),
                          (["item 1", "item 2", "item 3", "item 4"], "item 2", 2)])
def test_search_success_on_known_stack(stack_items, search_str, expected_return):
    new_stack = Stack()
    for item in stack_items:
        new_stack.push(item)
    assert new_stack.search(search_str) == expected_return

@pytest.mark.parametrize("stack_items, search_str, expected_return",
                         [(["item 1"], "bad data 1", -1),
                          (["item 1", "item 2", "item 3", "item 4"], "bad data 2", -1)])
def test_search_failure_on_known_stack(stack_items, search_str, expected_return):
    new_stack = Stack()
    for item in stack_items:
        new_stack.push(item)
    assert new_stack.search(search_str) == expected_return

@pytest.mark.parametrize("num_stack_items", [1,5])
def test_search_success_on_stack(num_stack_items):
    new_stack = make_stack(num_stack_items)
    search_item = stack_item_at(random.randint(1,num_stack_items))
    assert new_stack.search(search_item) >= 0


# __len__
@pytest.mark.parametrize("stack_size", range(6))
def test_len_on_stack(stack_size: int):
    new_stack = make_stack(stack_size)
    assert len(new_stack) == stack_size


# __bool__
def test_bool_empty_stack():
    new_stack = Stack()
    assert not new_stack

def test_bool_populated_stack():
    new_stack = make_stack(5)
    assert new_stack


# __eq__
@pytest.mark.parametrize("stack_size", range(5))
def test_eq_success(stack_size: int):
    stack_1 = make_stack(stack_size)
    stack_2 = make_stack(stack_size)
    assert stack_1 == stack_2
    assert stack_1 is not stack_2

@pytest.mark.parametrize("stack_1_size, stack_2_size",
                         [(1,0), (0,1), (3,40)])
def test_eq_fail(stack_1_size: int, stack_2_size: int):
    stack_1 = make_stack(stack_1_size)
    stack_2 = make_stack(stack_2_size)
    assert stack_1 != stack_2
    assert stack_1 is not stack_2


# __str__
def test_str_empty():
    new_stack = make_stack(0)
    assert str(new_stack) == "Stack (top -> bottom) : [  ]"

@pytest.mark.parametrize("stack_size, expected_str",
                         [(1, "Stack (top -> bottom) : [ item 1 ]"),
                          (2, "Stack (top -> bottom) : [ item 2, item 1 ]"),
                          (5, "Stack (top -> bottom) : [ item 5, item 4, item 3, item 2, item 1 ]")])
def test_str_with_values(stack_size: int,expected_str: str):
    new_stack = make_stack(stack_size)
    assert str(new_stack) == expected_str


# __repr__
def test_repr_empty():
    new_stack = make_stack(0)
    assert repr(new_stack) == "Stack (top -> bottom) : [  ]"

@pytest.mark.parametrize("stack_size, expected_str",
                         [(1, "Stack (top -> bottom) : [ item 1 ]"),
                          (2, "Stack (top -> bottom) : [ item 2, item 1 ]"),
                          (5, "Stack (top -> bottom) : [ item 5, item 4, item 3, item 2, item 1 ]")])
def test_repr_with_values(stack_size: int,expected_str: str):
    new_stack = make_stack(stack_size)
    assert repr(new_stack) == expected_str


