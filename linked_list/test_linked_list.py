from linked_list import LinkedList
from node import Node


def test_new_list_is_empty():
    test_list = LinkedList()

    assert test_list.head is None
    assert test_list.tail is None

def test_new_list_with_one_node():
    test_data = "test data"
    test_list = LinkedList()
    test_list.push(test_data)

    assert test_list.head is test_list.tail
    assert test_list.head.data == test_data

def test_add_new_node_to_existing_list():
    first_test_data = "first test data"
    second_test_data = "second test data"
    test_list = LinkedList()
    test_list.push(first_test_data)
    test_list.push(second_test_data)

    assert test_list.head is not test_list.tail
    assert test_list.head.data == first_test_data
    assert test_list.tail.data == second_test_data
    assert test_list.head.next_node is test_list.tail
    assert test_list.tail.prev_node is test_list.head
    assert test_list.head.prev_node is None
    assert test_list.tail.next_node is None
