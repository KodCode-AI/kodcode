class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def duplicate_linked_list(node):
    """
    Duplicates the given linked list.
    :param node: ListNode
    :return: ListNode
    """
    if not node:
        return None
    
    # Create a node with the same value
    new_head = ListNode(node.val)
    current_node = node
    new_current_node = new_head

    # Traverse the original linked list and create nodes for each value
    while current_node.next:
        new_next_node = ListNode(current_node.next.val)
        new_current_node.next = new_next_node
        current_node = current_node.next
        new_current_node = new_current_node.next

    return new_head