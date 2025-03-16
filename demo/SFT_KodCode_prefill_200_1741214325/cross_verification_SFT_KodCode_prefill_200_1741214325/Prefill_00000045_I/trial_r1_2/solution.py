class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def duplicate_linked_list(head):
    new_head = None
    new_tail = None
    current = head

    while current is not None:
        new_node = Node(current.value)
        if new_head is None:
            new_head = new_node
            new_tail = new_node
        else:
            new_tail.next = new_node
            new_tail = new_tail.next
        current = current.next

    return new_head