
import pytest

from deque import Deque
from deque_iterator import DequeIterator


def make_deque(items):
    new_deque = Deque()
    for item in items:
        new_deque.append(item)
    return new_deque


def test_empty_deque():
    new_deque = Deque()
    assert len(new_deque) == 0
    assert new_deque.size() == 0
    assert not new_deque
    assert new_deque.pop() is None
    assert new_deque.pop_left() is None
    assert new_deque.peek() is None
    assert new_deque.peek_left() is None

def test_one_item_queue():
    new_deque = make_deque(["cats"])
    assert new_deque.peek() == "cats"
    assert new_deque.peek_left() == "cats"
    assert len(new_deque) == 1
    assert new_deque

def test_append():
    new_deque = Deque()
    new_deque.append("cats")
    new_deque.append("dogs")
    new_deque.append("cows")
    assert len(new_deque) == 3
    assert new_deque.peek() == "cows"
    assert new_deque.peek_left() == "cats"
    assert list(new_deque) == ["cows", "dogs", "cats"]

def test_append_left():
    new_deque = Deque()
    new_deque.append_left("cats")
    new_deque.append_left("dogs")
    new_deque.append_left("cows")
    assert len(new_deque) == 3
    assert new_deque.peek() == "cats"
    assert new_deque.peek_left() == "cows"
    assert list(new_deque) == ["cats", "dogs", "cows"]

def test_pop():
    new_deque = make_deque(["cats", "dogs", "cows"])
    popped_val = new_deque.pop()
    assert popped_val == "cows"
    assert list(new_deque) == ["dogs", "cats"]

def test_pop_left():
    new_deque = make_deque(["cats", "dogs", "cows"])
    popped_val = new_deque.pop_left()
    assert popped_val == "cats"
    assert list(new_deque) == ["cows", "dogs"]

def test_peek():
    new_deque = make_deque(["cats", "dogs", "cows"])
    assert new_deque.peek() == "cows"

def test_peek_empty():
    new_deque = Deque()
    assert new_deque.peek() is None

def test_peek_left():
    new_deque = make_deque(["cats", "dogs", "cows"])
    assert new_deque.peek_left() == "cats"

def test_peek_left_empty():
    new_deque = Deque()
    assert new_deque.peek_left() is None

def test_clear():
    new_deque = make_deque(["cats", "dogs", "cows"])
    new_deque.clear()
    assert len(new_deque) == 0
    assert new_deque.size() == 0
    assert not new_deque
    assert new_deque.peek() is None
    assert new_deque.peek_left() is None
    assert new_deque.pop() is None
    assert new_deque.pop_left() is None

def test_reverse():
    new_deque = make_deque(["cats", "dogs", "cows"])
    reversed_items = make_deque(["cows", "dogs", "cats"])
    new_deque.reverse()
    assert new_deque == reversed_items
    assert list(new_deque) == ["cats", "dogs", "cows"]

def test_contains_true():
    new_deque = make_deque(["cats", "dogs", "cows"])
    assert "cats" in new_deque

def test_contains_false():
    new_deque = make_deque(["cats", "dogs", "cows"])
    assert "llamas" not in new_deque

@pytest.mark.parametrize("expected_size, deque_items",
                         [(0, []),
                         (1, ["cats"]),
                         (3, ["cats", "dogs", "cows"]),
                         (5, ["cats", "dogs", "cows", "weasels", "hobbits"])])
def test_size(expected_size, deque_items):
    new_deque = make_deque(deque_items)
    assert new_deque.size() == expected_size

@pytest.mark.parametrize("expected_size, deque_items",
                         [(0, []),
                         (1, ["cats"]),
                         (3, ["cats", "dogs", "cows"]),
                         (5, ["cats", "dogs", "cows", "weasels", "hobbits"])])
def test_len(expected_size, deque_items):
    new_deque = make_deque(deque_items)
    assert len(new_deque) == expected_size

def test_bool_true():
    new_deque = make_deque(["cats", "dogs", "cows"])
    assert new_deque

def test_bool_false():
    new_deque = Deque()
    assert not new_deque

@pytest.mark.parametrize("expected_str, items",
                         [("Deque[ ]", []),
                         ("Deque[ cats ]", ["cats"]),
                         ("Deque[ cows dogs cats ]", ["cats", "dogs", "cows"])])
def test_str(expected_str, items):
    new_deque = make_deque(items)
    assert str(new_deque) == expected_str

@pytest.mark.parametrize("expected_str, items",
                         [("Deque[ ]", []),
                         ("Deque[ cats ]", ["cats"]),
                         ("Deque[ cows dogs cats ]", ["cats", "dogs", "cows"])])
def test_repr(expected_str, items):
    new_deque = make_deque(items)
    assert repr(new_deque) == expected_str

@pytest.mark.parametrize(
    "deque1_items, deque2_items, expected",
    [([], [], True),
     (["cats"], [], False),
     (["cats"], ["cats"], True),
     (["cats"], ["dogs"], False),
     (["cats", "dogs", "cows"], ["dogs"], False),
     (["cats", "dogs", "cows"], ["cats", "dogs", "cows"], True),
     (["cats", "dogs", "cows"], ["cats", "llamas", "cows"], False),
     ])
def test_eq(deque1_items, deque2_items, expected):
    deque1 = make_deque(deque1_items)
    deque2 = make_deque(deque2_items)
    assert (deque1 == deque2) is expected

def test_eq_other_type():
    new_deque = make_deque(["cats", "dogs", "cows"])
    assert new_deque != ["cats", "dogs", "cows"]

def test_itererator_iter():
    new_iterator = DequeIterator(make_deque(["cats", "dogs", "cows"]))
    assert iter(new_iterator) is new_iterator