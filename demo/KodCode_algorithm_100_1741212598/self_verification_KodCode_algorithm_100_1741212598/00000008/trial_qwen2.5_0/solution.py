class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

def detect_cycle(linked_list: LinkedList) -> bool:
    if not linked_list.head:
        return False

    slow_runner = linked_list.head
    fast_runner = linked_list.head

    while fast_runner and fast_runner.next_node:
        slow_runner = slow_runner.next_node
        fast_runner = fast_runner.next_node.next_node

        if slow_runner == fast_runner:
            return True

    return False