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
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev