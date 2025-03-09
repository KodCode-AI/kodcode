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
    Returns True if a cycle exists in the linked list using Floyd's cycle detection algorithm.
    """
    if not linked_list.head:
        return False

    slow = linked_list.head
    fast = linked_list.head

    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow == fast:
            return True

    return False