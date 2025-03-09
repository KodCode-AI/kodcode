class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    """
    Reverses a linked list in place.
    
    Args:
    head (ListNode): The head node of the linked list.
    
    Returns:
    ListNode: The new head of the reversed linked list.
    """
    prev = None
    current = head
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev and current one step forward
        current = next_node
    return prev