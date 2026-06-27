from linked_list import LinkedList
import pytest


NODE_ONE_DATA = "node one test data"
NODE_TWO_DATA = "node two test data"

# Fixtures
@pytest.fixture
def empty_list():
    return LinkedList()

@pytest.fixture
def list_with_one_node(empty_list):
    empty_list.push(NODE_ONE_DATA)
    return empty_list

@pytest.fixture
def list_with_two_nodes(list_with_one_node):
    list_with_one_node.push(NODE_TWO_DATA)
    return list_with_one_node


# Testing list itself, __init__()
def test_new_list_is_empty(empty_list):
    assert empty_list.head is None
    assert empty_list.tail is None
    assert empty_list.size == 0


# Testing add() method
def test_new_empty_list_add_one_node():
    test_list = LinkedList()
    test_list.push(NODE_ONE_DATA)
    assert test_list.head is test_list.tail
    assert test_list.head.data == NODE_ONE_DATA
    assert test_list.size == 1

def test_add_new_node_to_existing_list():
    test_list = LinkedList()
    test_list.push(NODE_ONE_DATA)
    test_list.push(NODE_TWO_DATA)

    assert test_list.head is not test_list.tail
    assert test_list.head.data == NODE_ONE_DATA
    assert test_list.tail.data == NODE_TWO_DATA
    assert test_list.head.next_node is test_list.tail
    assert test_list.tail.prev_node is test_list.head
    assert test_list.head.prev_node is None
    assert test_list.tail.next_node is None


# Testing pop() method
def test_pop_when_list_empty(empty_list):
    with pytest.raises(IndexError):
        empty_list.pop()
    assert empty_list.size == 0

def test_pop_when_list_has_one_node(list_with_one_node):
    pop_return_value = list_with_one_node.pop()

    assert pop_return_value == NODE_ONE_DATA
    assert list_with_one_node.head is None
    assert list_with_one_node.tail is None
    assert list_with_one_node.size == 0

def test_pop_when_list_has_two_nodes(list_with_two_nodes):
    head_node = list_with_two_nodes.head
    pop_result = list_with_two_nodes.pop()

    assert pop_result == NODE_TWO_DATA
    assert list_with_two_nodes.head is head_node
    assert list_with_two_nodes.tail is head_node
    assert head_node.next_node is None
    assert list_with_two_nodes.size == 1


# Testing _node_at_index() method
def test_node_at_index_when_list_has_one_node(list_with_one_node):
    assert list_with_one_node._node_at_index(0) is list_with_one_node.head

def test_node_at_index_when_list_has_two_nodes(list_with_two_nodes):
    assert list_with_two_nodes._node_at_index(0) is list_with_two_nodes.head
    assert list_with_two_nodes._node_at_index(1) is list_with_two_nodes.tail


# Testing __len__() method
def test_len_when_list_empty(empty_list):
    assert len(empty_list) == 0

def test_len_when_list_has_one_node(list_with_one_node):
    assert len(list_with_one_node) == 1

def test_len_when_list_has_two_nodes(list_with_two_nodes):
    assert len(list_with_two_nodes) == 2


# Testing iterator
def test_iter_when_list_empty(empty_list):
    assert list(empty_list) == []

def test_iter_when_list_has_one_node(list_with_one_node):
    assert list(list_with_one_node) == [NODE_ONE_DATA]

def test_iter_when_list_has_two_nodes(list_with_two_nodes):
    assert list(list_with_two_nodes) == [NODE_ONE_DATA, NODE_TWO_DATA]