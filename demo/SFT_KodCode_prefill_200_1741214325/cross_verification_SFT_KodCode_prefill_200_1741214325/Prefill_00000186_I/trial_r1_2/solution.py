class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    stack = []
    current = head
    
    # Push all nodes onto the stack
    while current is not None:
        stack.append(current)
        current = current.next
    
    # Create a dummy node to build the reversed list
    dummy = Node()
    current = dummy
    
    # Pop nodes from the stack and build the reversed list
    while stack:
        node = stack.pop()
        current.next = node
        current = current.next
    
    # Set the last node's next to None to terminate the list
    current.next = None
    
    # The reversed list starts from dummy's next node
    return dummy.next