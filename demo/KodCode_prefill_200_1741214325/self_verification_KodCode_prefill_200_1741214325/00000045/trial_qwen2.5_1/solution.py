class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def duplicate_linked_list(head):
    """
    Duplicates a linked list including values and next pointers.
    """
    if not head:
        return None
    
    current = head
    while current:
        new_node = ListNode(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next
    
    current = head
    copy_head = None
    copy_current = None
    
    while current:
        if not copy_head:
            copy_head = copy_current = current.next
        else:
            copy_current.next = current.next.next
            copy_current = copy_current.next
        current.next = current.next.next
        current = current.next
    
    return copy_head