class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    stack = []
    current = head
    # Push all nodes onto the stack
    while current is not None:
        stack.append(current)
        current = current.next
    # Create a dummy node to help build the reversed list
    dummy = Node(0)
    current_reversed = dummy
    # Pop nodes and build the reversed list
    while stack:
        popped_node = stack.pop()
        popped_node.next = None
        current_reversed.next = popped_node
        current_reversed = current_reversed.next
    return dummy.next