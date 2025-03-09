class ListNode:
    """Simple linked list node class."""
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    """
    Reverses a linked list in-place using a stack to temporarily store nodes.
    
    :param head: ListNode, the head of the linked list to be reversed
    :return: ListNode, the new head of the reversed linked list
    """
    stack = []
    current = head
    while current:
        stack.append(current)
        current = current.next
    
    # If the list was empty, return None or the last node.
    if not stack:
        return None
    
    new_head = stack.pop()
    current = new_head
    while stack:
        current.next = stack.pop()
        current = current.next
    current.next = None
    
    return new_head