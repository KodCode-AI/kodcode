class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def duplicate_linked_list(head):
    if not head:
        return None

    new_head = Node(head.val)
    current_new = new_head
    current_original = head.next

    while current_original:
        new_node = Node(current_original.val)
        current_new.next = new_node
        current_new = new_node
        current_original = current_original.next

    return new_head