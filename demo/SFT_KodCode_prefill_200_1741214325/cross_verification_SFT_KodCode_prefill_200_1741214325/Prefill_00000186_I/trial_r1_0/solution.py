class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    if not head:
        return None
    
    stack = []
    current = head
    
    # Push all elements of the linked list onto the stack
    while current:
        stack.append(current.data)
        current = current.next
    
    reversed_head = None
    current_node = None
    
    # Pop elements from the stack and build the reversed linked list
    while stack:
        data = stack.pop()
        new_node = Node(data)
        if reversed_head is None:
            reversed_head = new_node
            current_node = reversed_head
        else:
            current_node.next = new_node
            current_node = new_node
    
    return reversed_head