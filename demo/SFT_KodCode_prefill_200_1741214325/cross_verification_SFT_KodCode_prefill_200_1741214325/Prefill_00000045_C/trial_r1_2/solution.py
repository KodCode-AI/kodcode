class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def duplicate_linked_list(node: ListNode) -> ListNode:
    if not node:
        return None
    new_head = ListNode(node.val)
    new_current = new_head
    current = node.next
    while current:
        new_node = ListNode(current.val)
        new_current.next = new_node
        new_current = new_node
        current = current.next
    return new_head