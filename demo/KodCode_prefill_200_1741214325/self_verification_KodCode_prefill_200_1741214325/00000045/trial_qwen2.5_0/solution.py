class ListNode:
    """Simple linked list node class."""
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def duplicate_linked_list(head):
    """
    Duplicates the linked list including both the node values and the next pointers.
    """
    if head is None:
        return None
    
    # Create a dummy node to help with the initial insertion
    current_original = head
    dummy = ListNode(0)
    current_duplicated = dummy
    
    # Dictionary to store the mapping of original nodes to new nodes
    mapping = {None: None}
    
    while current_original is not None:
        new_node = ListNode(current_original.value)
        current_duplicated.next = new_node
        mapping[current_original] = new_node
        
        current_original = current_original.next
        current_duplicated = current_duplicated.next
    
    # Set up the next pointers of the duplicated list
    current_detailed = dummy.next
    current_original = head
    while current_detailed is not None:
        current_detailed.next = mapping[current_original.next]
        current_original = current_original.next
        current_detailed = current_detailed.next
    
    return dummy.next