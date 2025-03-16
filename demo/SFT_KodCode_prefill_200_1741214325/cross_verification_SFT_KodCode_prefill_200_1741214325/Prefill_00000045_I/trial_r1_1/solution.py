class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def duplicate_linked_list(head):
    if not head:
        return None
    
    # Initialize the new head with the data of the original head
    new_head = Node(head.data)
    new_current = new_head
    
    # Traverse the original linked list starting from the second node
    current = head.next
    
    while current:
        # Create a new node with the same data as current node
        new_node = Node(current.data)
        # Link the new node to the new_current's next
        new_current.next = new_node
        # Move to the newly created node
        new_current = new_node
        # Move to the next node in the original list
        current = current.next
    
    return new_head