class LinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next_node = None
    
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        if not self.head:
            self.head = self.Node(data)
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = self.Node(data)

def detect_cycle(linked_list):
    if linked_list.head is None:
        return False
    slow = linked_list.head
    fast = linked_list.head
    while fast is not None and fast.next_node is not None:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow == fast:
            return True
    return False