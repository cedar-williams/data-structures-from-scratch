import pytest
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


def test_empty_on_empty_stack():
    new_stack = Stack()
    assert new_stack.empty() is True

@pytest.mark.parametrize("num_stack_items", [1,2,10,100])
def test_empty_on_stack_with_items(num_stack_items):
    new_stack = make_stack(num_stack_items)
    assert new_stack.empty() is False

def test_peek_on_empty_stack():
    new_stack = Stack()
    with pytest.raises(IndexError):
        new_stack.peek()

@pytest.mark.parametrize("num_stack_items", [1,2,3,4,5,10,20,100])
def test_peek_on_stack_with_items(num_stack_items):
    new_stack = make_stack(num_stack_items)
    assert new_stack.peek() == stack_item_at(num_stack_items)

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