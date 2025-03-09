class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    """
    Reverses a linked list in place.
    
    :param head: ListNode, the head of the linked list to be reversed.
    :return: ListNode, the new head of the reversed linked list.
    """
    prev = None
    current = head
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move pointers one position forward
        current = next_node
    return prev