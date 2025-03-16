class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    if not head:
        return None
    
    stack = []
    current = head
    while current:
        stack.append(current)
        current = current.next
    
    dummy = ListNode(0)
    new_head = dummy
    
    while stack:
        node = stack.pop()
        dummy.next = node
        node.next = None
        dummy = dummy.next
    
    return new_head.next