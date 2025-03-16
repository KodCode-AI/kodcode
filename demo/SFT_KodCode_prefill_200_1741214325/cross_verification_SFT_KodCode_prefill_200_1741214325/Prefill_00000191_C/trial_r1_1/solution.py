class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev