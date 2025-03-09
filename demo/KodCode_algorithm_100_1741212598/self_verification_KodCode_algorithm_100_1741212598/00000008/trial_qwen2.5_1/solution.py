class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = Node(value)

def detect_cycle(linked_list: LinkedList) -> bool:
    """
    Detects whether a cycle exists in the linked list using Floyd's cycle detection algorithm.
    """
    if not linked_list.head or not linked_list.head.next_node:
        return False

    slow_pointer = linked_list.head
    fast_pointer = linked_list.head

    while fast_pointer and fast_pointer.next_node:
        slow_pointer = slow_pointer.next_node
        fast_pointer = fast_pointer.next_node.next_node
        if slow_pointer == fast_pointer:
            return True

    return False