class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse_linked_list(head: ListNode) -> ListNode:
    """
    Reverses a linked list in-place using a stack to temporarily store nodes.
    
    :param head: ListNode, the head of the linked list to be reversed
    :return: ListNode, the new head of the reversed linked list
    """
    if not head:
        return None
    
    stack = []
    current = head
    # Push all nodes onto the stack
    while current:
        stack.append(current)
        current = current.next
    
    # Reversed list is built by popping nodes from the stack
    dummy = ListNode(0)
    tail = dummy
    while stack:
        current_node = stack.pop()
        tail.next = current_node
        tail = tail.next
    # Ensure the end of the reversed list
    tail.next = None
    
    return dummy.next