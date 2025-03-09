class ListNode:
    """Simple linked list node class."""
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    """
    Reverses a linked list in place and returns the new head.
    
    :param head: ListNode
        The head node of the linked list to be reversed.
    :return: ListNode
        The new head node of the reversed linked list.
    """
    prev = None
    current = head
    while current:
        next_node = current.next  # Store next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move prev and current one step forward
        current = next_node
    return prev