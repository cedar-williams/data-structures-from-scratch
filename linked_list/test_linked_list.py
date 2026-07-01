from pygments.lexers import oberon

from linked_list import LinkedList
import pytest

NODE_DUPLICATE_DATA = "node duplicate"

NODE_ONE_DATA = "node one"
NODE_TWO_DATA = "node two"
NODE_THREE_DATA = "node three"

UPDATED_NODE_ONE_DATA = "updated node one"
UPDATED_NODE_TWO_DATA = "updated node two"

NODE_ONE_INSERT_DATA = "insert node one"
NODE_TWO_INSERT_DATA = "insert node two"
NODE_THREE_INSERT_DATA = "insert node three"

DATA_NOT_IN_ANY_NODE = "bad data"

def linked_list_to_backwards_list(linked_list: LinkedList) -> list:
    return_list = []
    cur_node = linked_list.tail
    while cur_node is not None:
        return_list.append(cur_node.data)
        cur_node = cur_node.prev_node
    return return_list

# Fixtures
@pytest.fixture
def empty_list():
    return LinkedList()

@pytest.fixture
def another_empty_list():
    return LinkedList()

@pytest.fixture
def list_with_one_node():
    temp_list = LinkedList()
    temp_list.push(NODE_ONE_DATA)
    return temp_list

@pytest.fixture
def list_with_two_nodes():
    temp_list = LinkedList()
    temp_list.push(NODE_ONE_DATA)
    temp_list.push(NODE_TWO_DATA)
    return temp_list

@pytest.fixture
def list_with_two_nodes_backwards():
    temp_list = LinkedList()
    temp_list.push(NODE_TWO_DATA)
    temp_list.push(NODE_ONE_DATA)
    return temp_list

@pytest.fixture
def list_with_three_nodes():
    temp_list = LinkedList()
    temp_list.push(NODE_ONE_DATA)
    temp_list.push(NODE_TWO_DATA)
    temp_list.push(NODE_THREE_DATA)
    return temp_list

@pytest.fixture
def another_list_with_three_nodes():
    temp_list = LinkedList()
    temp_list.push(NODE_ONE_DATA)
    temp_list.push(NODE_TWO_DATA)
    temp_list.push(NODE_THREE_DATA)
    return temp_list

@pytest.fixture
def list_with_three_nodes_backwards():
    temp_list = LinkedList()
    temp_list.push(NODE_THREE_DATA)
    temp_list.push(NODE_TWO_DATA)
    temp_list.push(NODE_ONE_DATA)
    return temp_list

@pytest.fixture
def list_with_three_nodes_identical():
    list_obj = LinkedList()
    list_obj.push(NODE_DUPLICATE_DATA)
    list_obj.push(NODE_DUPLICATE_DATA)
    list_obj.push(NODE_DUPLICATE_DATA)
    return list_obj


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
@pytest.mark.parametrize("index", [-1,1])
def test_insert_invalid_index_list_is_empty(empty_list, index):
    with pytest.raises(IndexError):
        empty_list.insert(index, "data")
    assert empty_list.size == 0
    assert list(empty_list) == []

def test_insert_valid_index_list_is_empty(empty_list):
    empty_list.insert(0, NODE_ONE_INSERT_DATA)
    assert empty_list.head is empty_list.tail
    assert empty_list.get(0) == NODE_ONE_INSERT_DATA
    assert list(empty_list) == [NODE_ONE_INSERT_DATA]
    assert empty_list.size == 1
    assert len(empty_list) == 1

@pytest.mark.parametrize("index", [-1,2])
def test_insert_invalid_index_when_list_has_one_node(list_with_one_node, index):
    with pytest.raises(IndexError):
        list_with_one_node.insert(index, "data")
    assert list_with_one_node.size == 1
    assert list(list_with_one_node) == [NODE_ONE_DATA]

@pytest.mark.parametrize("index, new_data, expected_list",
                        [(0, NODE_ONE_INSERT_DATA, [NODE_ONE_INSERT_DATA, NODE_ONE_DATA]),
                         (1, NODE_TWO_INSERT_DATA, [NODE_ONE_DATA, NODE_TWO_INSERT_DATA])])
def test_insert_valid_index_when_list_has_one_node(list_with_one_node, index, new_data, expected_list):
    list_with_one_node.insert(index, new_data)

    assert list_with_one_node.size == 2
    assert list(list_with_one_node) == expected_list


@pytest.mark.parametrize("index", [-1,3])
def test_insert_invalid_index_when_list_has_two_nodes(list_with_two_nodes, index):
    with pytest.raises(IndexError):
        list_with_two_nodes.insert(index, "data")
    assert list_with_two_nodes.size == 2
    assert list(list_with_two_nodes) == [NODE_ONE_DATA, NODE_TWO_DATA]

@pytest.mark.parametrize("index, new_data, expected_list",
                        [(0, NODE_ONE_INSERT_DATA, [NODE_ONE_INSERT_DATA, NODE_ONE_DATA, NODE_TWO_DATA]),
                         (1, NODE_TWO_INSERT_DATA, [NODE_ONE_DATA, NODE_TWO_INSERT_DATA, NODE_TWO_DATA]),
                         (2, NODE_THREE_INSERT_DATA, [NODE_ONE_DATA, NODE_TWO_DATA, NODE_THREE_INSERT_DATA])])
def test_insert_valid_index_when_list_has_two_nodes(list_with_two_nodes, index, new_data, expected_list):
    list_with_two_nodes.insert(index, new_data)
    assert list(list_with_two_nodes) == expected_list
    assert list_with_two_nodes.size == 3

def test_insert_in_middle_of_two_nodes(list_with_two_nodes):
    old_head = list_with_two_nodes.head
    old_tail = list_with_two_nodes.tail
    list_with_two_nodes.insert(1, NODE_TWO_INSERT_DATA)
    new_node = list_with_two_nodes._node_at_index(1)
    assert list_with_two_nodes.head is old_head
    assert list_with_two_nodes.tail is old_tail
    assert list_with_two_nodes.head.next_node is new_node
    assert list_with_two_nodes.tail.prev_node is new_node
    assert new_node.next_node is list_with_two_nodes.tail
    assert new_node.prev_node is list_with_two_nodes.head


# Testing remove() method
@pytest.mark.parametrize("index", [-1,0,1])
def test_remove_list_empty(empty_list, index):
    with pytest.raises(IndexError):
        empty_list.remove(index)
    assert empty_list.size == 0
    assert list(empty_list) == []

@pytest.mark.parametrize("index", [-1,1])
def test_remove_invalid_index_list_with_one_node(list_with_one_node, index):
    with pytest.raises(IndexError):
        list_with_one_node.remove(index)
    assert list_with_one_node.size == 1
    assert list(list_with_one_node) == [NODE_ONE_DATA]
    assert len(list_with_one_node) == 1

def test_remove_valid_index_list_with_one_node(list_with_one_node):
    return_val = list_with_one_node.remove(0)

    assert list_with_one_node.size == 0
    assert list(list_with_one_node) == []
    assert list_with_one_node.head is None
    assert list_with_one_node.tail is None
    assert return_val == NODE_ONE_DATA

@pytest.mark.parametrize("index", [-1,2])
def test_remove_invalid_index_list_with_two_nodes(list_with_two_nodes, index):
    with pytest.raises(IndexError):
        list_with_two_nodes.remove(index)

    assert list_with_two_nodes.size == 2
    assert list(list_with_two_nodes) == [NODE_ONE_DATA, NODE_TWO_DATA]
    assert len(list_with_two_nodes) == 2

@pytest.mark.parametrize("index, expected_return, expected_remaining_list",
                         [(0, NODE_ONE_DATA, [NODE_TWO_DATA]),
                          (1, NODE_TWO_DATA, [NODE_ONE_DATA])])
def test_remove_valid_index_list_with_two_nodes(list_with_two_nodes, index, expected_return, expected_remaining_list):
    return_val = list_with_two_nodes.remove(index)

    assert return_val == expected_return
    assert list_with_two_nodes.size == 1
    assert len(list_with_two_nodes) == 1
    assert list(list_with_two_nodes) == expected_remaining_list

def test_remove_from_middle_of_three_nodes(list_with_three_nodes):
    return_val = list_with_three_nodes.remove(1)

    assert return_val == NODE_TWO_DATA
    assert list_with_three_nodes.size == 2
    assert len(list_with_three_nodes) == 2
    assert list(list_with_three_nodes) == [NODE_ONE_DATA, NODE_THREE_DATA]
    assert list_with_three_nodes.head.next_node is list_with_three_nodes.tail
    assert list_with_three_nodes.tail.prev_node is list_with_three_nodes.head


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


# Testing clear() method
def test_clear_empty_list(empty_list):
    empty_list.clear()
    assert empty_list.size == 0
    assert empty_list.head is None
    assert empty_list.tail is None
    assert list(empty_list) == []

def test_clear_populated_list(list_with_two_nodes):
    list_with_two_nodes.clear()
    assert list_with_two_nodes.size == 0
    assert list_with_two_nodes.head is None
    assert list_with_two_nodes.tail is None
    assert list(list_with_two_nodes) == []


# Testing index() method
def test_index_with_empty_list(empty_list):
    with pytest.raises(ValueError):
        empty_list.index(DATA_NOT_IN_ANY_NODE)
    assert len(empty_list) == 0

def test_index_invalid_data_with_list_with_three_nodes(list_with_three_nodes):
    with pytest.raises(ValueError):
        list_with_three_nodes.index(DATA_NOT_IN_ANY_NODE)
    assert len(list_with_three_nodes) == 3

@pytest.mark.parametrize("search_data, expected_index",
                         [(NODE_ONE_DATA, 0),
                          (NODE_TWO_DATA, 1),
                          (NODE_THREE_DATA, 2)])
def test_index_valid_data_with_list_with_three_nodes(list_with_three_nodes, search_data, expected_index):
    index_result = list_with_three_nodes.index(search_data)
    assert index_result == expected_index
    assert len(list_with_three_nodes) == 3
    assert list(list_with_three_nodes) == [NODE_ONE_DATA, NODE_TWO_DATA, NODE_THREE_DATA]

def test_index_invalid_data_with_list_with_three_nodes_identical(list_with_three_nodes_identical):
    with pytest.raises(ValueError):
        list_with_three_nodes_identical.index(DATA_NOT_IN_ANY_NODE)

def test_index_valid_data_with_list_with_three_nodes_identical(list_with_three_nodes_identical):
    index_result = list_with_three_nodes_identical.index(NODE_DUPLICATE_DATA)
    assert index_result == 0


# Testing reverse() method
def test_reverse_empty_list(empty_list):
    empty_list.reverse()
    assert list(empty_list) == []

def test_reverse_list_with_one_node(list_with_one_node):
    initial_state = list(list_with_one_node)
    list_with_one_node.reverse()
    assert list(list_with_one_node) == initial_state

def test_reverse_list_with_two_nodes(list_with_two_nodes, list_with_two_nodes_backwards):
    list_with_two_nodes.reverse()
    assert list(list_with_two_nodes) == list(list_with_two_nodes_backwards)

def test_reverse_list_with_three_nodes(list_with_three_nodes, list_with_three_nodes_backwards):
    comparison_list = linked_list_to_backwards_list(list_with_three_nodes)
    list_with_three_nodes.reverse()

    assert list(list_with_three_nodes) == list(list_with_three_nodes_backwards)
    assert list(list_with_three_nodes) == comparison_list

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


# Test __eq__() dunder method
def test_eq_empty_list(empty_list, another_empty_list):
    assert empty_list is not another_empty_list
    assert empty_list == another_empty_list

def test_eq_nonmatching_lists_with_different_sizes(empty_list, list_with_three_nodes):
    assert empty_list is not list_with_three_nodes
    assert empty_list != list_with_three_nodes

def test_eq_list_with_three_nodes(list_with_three_nodes, another_list_with_three_nodes):
    assert list_with_three_nodes is not another_list_with_three_nodes
    assert list_with_three_nodes == another_list_with_three_nodes

def test_eq_same_size_diff_order(list_with_three_nodes, list_with_three_nodes_identical):
    assert list_with_three_nodes is not list_with_three_nodes_identical
    assert list_with_three_nodes != list_with_three_nodes_identical


# Test __contains__() dunder method
def test_contains_empty_list(empty_list):
    assert NODE_ONE_DATA not in empty_list

def test_contains_no_match_single_item_list(list_with_one_node):
    assert DATA_NOT_IN_ANY_NODE not in list_with_one_node

def test_contains_match_single_item_list(list_with_one_node):
    assert NODE_ONE_DATA in list_with_one_node

def test_contains_no_match_three_node_list(list_with_three_nodes):
    assert DATA_NOT_IN_ANY_NODE not in list_with_three_nodes

@pytest.mark.parametrize("node_data", [NODE_ONE_DATA, NODE_TWO_DATA, NODE_THREE_DATA])
def test_contains_match_three_node_list(list_with_three_nodes, node_data):
    assert node_data in list_with_three_nodes


# Test getitem, setitem, delitem dunder methods
def test_getitem_valid_index(list_with_three_nodes):
    assert list_with_three_nodes[0] == NODE_ONE_DATA

def test_getitem_invalid_index(list_with_three_nodes):
    with pytest.raises(IndexError):
        result = list_with_three_nodes[5]

def test_setitem_valid_index(list_with_three_nodes):
    list_with_three_nodes[0] = NODE_ONE_INSERT_DATA
    assert list_with_three_nodes.get(0) == NODE_ONE_INSERT_DATA

def test_setitem_invalid_index(list_with_three_nodes):
    with pytest.raises(IndexError):
        list_with_three_nodes[5] = DATA_NOT_IN_ANY_NODE

def test_delitem_valid_index(list_with_three_nodes):
    del list_with_three_nodes[1]
    assert list(list_with_three_nodes) == [NODE_ONE_DATA, NODE_THREE_DATA]

def test_delitem_invalid_index(list_with_three_nodes):
    with pytest.raises(IndexError):
        del list_with_three_nodes[5]


