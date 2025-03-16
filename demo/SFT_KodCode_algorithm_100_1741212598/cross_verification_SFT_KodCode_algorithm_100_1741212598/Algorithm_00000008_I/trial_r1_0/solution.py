class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

def detect_cycle(linked_list: LinkedList) -> bool:
    if linked_list.head is None:
        return False

    slow_ptr = linked_list.head
    fast_ptr = linked_list.head

    while True:
        # Move slow pointer one step
        slow_ptr = slow_ptr.next_node

        if fast_ptr is None or fast_ptr.next_node is None:
            break  # Reached end, no cycle

        # Move fast pointer two steps
        fast_ptr = fast_ptr.next_node.next_node

        if slow_ptr == fast_ptr:
            return True

    return False