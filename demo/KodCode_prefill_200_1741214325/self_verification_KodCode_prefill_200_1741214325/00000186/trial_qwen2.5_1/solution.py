class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list_with_stack(head):
    """
    Reverses a linked list by using a stack data structure.
    """
    if not head:
        return None
    
    stack = []
    current = head
    # Push all elements of the linked list onto the stack
    while current:
        stack.append(current)
        current = current.next
    
    if not stack:
        return None
    
    # Pop elements from the stack to form the reversed linked list
    new_head = stack.pop()
    current = new_head
    while stack:
        current.next = stack.pop()
        current = current.next
    current.next = None
    
    return new_head