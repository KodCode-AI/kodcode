class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def duplicate_linked_list(node: ListNode) -> ListNode:
    if not node:
        return None
    dummy = ListNode()
    current = dummy
    while node:
        current.next = ListNode(node.val)
        current = current.next
        node = node.next
    return dummy.next