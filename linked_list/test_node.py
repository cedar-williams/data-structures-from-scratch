from node import Node

def test_new_node_is_empty():
    test_node = Node("test string")

    assert test_node.data == "test string"
    assert test_node.next_node is None
    assert test_node.prev_node is None