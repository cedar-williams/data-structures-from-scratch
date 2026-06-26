from node import Node

class LinkedList:
    """Linked list implementation"""

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data) -> None:
        """Add a new node at end of list
        :param data: the value or object to be added to the LinkedList"""
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            node.prev_node = self.tail
            self.tail = node