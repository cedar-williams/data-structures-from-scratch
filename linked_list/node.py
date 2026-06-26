class Node:
    """A single node in a linked list, storing a data value and next/prev pointers."""
    def __init__(self, data, prev_node = None, next_node = None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node