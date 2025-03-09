class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list_with_stack(head):
    """
    Reverses the given linked list using a stack data structure.
    """
    if head is None:
        return None
    
    stack = []
    current = head
    while current:
        stack.append(current)
        current = current.next
    
    if not stack:
        return None
    
    new_head = stack.pop()
    current = new_head
    while stack:
        current.next = stack.pop()
        current = current.next
    current.next = None
    
    return new_head