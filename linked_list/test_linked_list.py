from linked_list import LinkedList
import pytest


NODE_ONE_DATA = "node one"
NODE_TWO_DATA = "node two"

UPDATED_NODE_ONE_DATA = "updated node one"
UPDATED_NODE_TWO_DATA = "updated node two"

NODE_ONE_INSERT_DATA = "insert node one"
NODE_TWO_INSERT_DATA = "insert node two"

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


# Testing insert() method
@pytest.mark.parametrize("index", [-1,0,1])
def test_insert_list_is_empty(empty_list, index):
    with pytest.raises(IndexError):
        empty_list.insert(index, "data")
    assert empty_list.size == 0

@pytest.mark.parametrize("index", [-1,1])
def test_insert_invalid_index_when_list_has_one_node(list_with_one_node, index):
    with pytest.raises(IndexError):
        list_with_one_node.insert(index, "data")
    assert list_with_one_node.size == 1

def test_insert_valid_index_when_list_has_one_node(list_with_one_node):
    list_with_one_node.insert(0, NODE_ONE_INSERT_DATA)

    assert list(list_with_one_node) == [NODE_ONE_INSERT_DATA, NODE_ONE_DATA]
    assert list_with_one_node.size == 2

@pytest.mark.parametrize("index", [-1,2])
def test_insert_invalid_index_when_list_has_two_nodes(list_with_two_nodes, index):
    with pytest.raises(IndexError):
        list_with_two_nodes.insert(index, "data")
    assert list_with_two_nodes.size == 2

@pytest.mark.parametrize("index, new_data, expected_list",
                        [(0, NODE_ONE_INSERT_DATA, [NODE_ONE_INSERT_DATA, NODE_ONE_DATA, NODE_TWO_DATA]),
                         (1, NODE_TWO_INSERT_DATA, [NODE_ONE_DATA, NODE_TWO_INSERT_DATA, NODE_TWO_DATA])])
def test_insert_valid_index_when_list_has_two_nodes(list_with_two_nodes, index, new_data, expected_list):
    list_with_two_nodes.insert(index, new_data)
    assert list(list_with_two_nodes) == expected_list
    assert list_with_two_nodes.size == 3

# Testing remove() method

# Testing get() method
@pytest.mark.parametrize("index", [-1,0,1])
def test_get_index_when_list_empty(empty_list, index):
    with pytest.raises(IndexError):
        empty_list.get(index)
    assert empty_list.size == 0

@pytest.mark.parametrize("index", [-1,1])
def test_get_invalid_index_when_list_has_one_node(list_with_one_node, index):
    with pytest.raises(IndexError):
        list_with_one_node.get(index)
    assert list_with_one_node.size == 1

def test_get_valid_index_when_list_has_one_node(list_with_one_node):
    assert list_with_one_node.get(0) == NODE_ONE_DATA
    assert list_with_one_node.size == 1

@pytest.mark.parametrize("index", [-1,2])
def test_get_invalid_index_when_list_has_two_nodes(list_with_two_nodes, index):
    with pytest.raises(IndexError):
        list_with_two_nodes.get(index)
    assert list_with_two_nodes.size == 2

@pytest.mark.parametrize("index, expected",
    [(0, NODE_ONE_DATA), (1, NODE_TWO_DATA)])
def test_get_valid_index_when_list_has_two_nodes(list_with_two_nodes, index, expected):
    assert list_with_two_nodes.get(index) == expected
    assert list_with_two_nodes.size == 2


# Testing set() method
@pytest.mark.parametrize("index", [-1,0,1])
def test_set_index_when_list_empty(empty_list, index):
    with pytest.raises(IndexError):
        empty_list.set(index, "data")

@pytest.mark.parametrize("index", [-1,1])
def test_set_invalid_index_when_list_has_one_node(list_with_one_node, index):
    with pytest.raises(IndexError):
        list_with_one_node.set(index, "data")

def test_set_valid_index_when_list_has_one_node(list_with_one_node):
    list_with_one_node.set(0, UPDATED_NODE_ONE_DATA)
    assert list_with_one_node.get(0) == UPDATED_NODE_ONE_DATA
    assert list(list_with_one_node) == [UPDATED_NODE_ONE_DATA]
    assert list_with_one_node.size == 1

@pytest.mark.parametrize("index", [-1,2])
def test_set_invalid_index_when_list_has_two_nodes(list_with_two_nodes, index):
    with pytest.raises(IndexError):
        list_with_two_nodes.set(index, "data")

@pytest.mark.parametrize("index, new_data, expected_list",
                         [(0, UPDATED_NODE_ONE_DATA, [UPDATED_NODE_ONE_DATA,NODE_TWO_DATA]),
                          (1, UPDATED_NODE_TWO_DATA, [NODE_ONE_DATA, UPDATED_NODE_TWO_DATA])])
def test_set_valid_index_when_list_has_two_nodes(list_with_two_nodes, index, new_data, expected_list):
    list_with_two_nodes.set(index, new_data)
    assert list_with_two_nodes.get(index) == new_data
    assert list_with_two_nodes.size == 2
    assert list(list_with_two_nodes) == expected_list


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