class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def duplicate_linked_list(node: ListNode) -> ListNode:
    """Duplicates the given linked list."""
    if node is None:
        return None
    new_head = ListNode(node.val)
    tail = new_head
    current = node.next
    while current:
        tail.next = ListNode(current.val)
        tail = tail.next
        current = current.next
    return new_head