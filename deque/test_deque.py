
import pytest

from deque import Deque


def test_empty_deque():
    new_deque = Deque()
    assert len(new_deque) == 0
    assert not new_deque
    assert new_deque.pop() is None
    assert new_deque.pop_left() is None

def test_one_item_queue():
    new_deque = Deque()
    new_deque.append("cats")
    assert new_deque.peek() == "cats"
    assert new_deque.peek_left() == "cats"
    assert len(new_deque) == 1
    assert new_deque