from solution import *

from solution import ListNode, reverse_linked_list_with_stack
from typing import Optional

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def to_list(head: Optional[ListNode]) -> list:
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

def test_reverse_linked_list_with_stack():
    # Single element list
    head = ListNode(1)
    assert to_list(reverse_linked_list_with_stack(head)) == [1]
    
    # Empty list
    head = None
    assert reverse_linked_list_with_stack(head) is None
    
    # Multiple elements
    head = create_linked_list([1, 2, 3, 4, 5])
    assert to_list(reverse_linked_list_with_stack(head)) == [5, 4, 3, 2, 1]
    
    # Reversing a linked list with nodes having the same value
    head = create_linked_list([1, 1, 1])
    assert to_list(reverse_linked_list_with_stack(head)) == [1, 1, 1]
    
    # Reversing a linked list formed in a zigzag pattern
    head = create_linked_list([1, 3, 2, 4, 5])
    assert to_list(reverse_linked_list_with_stack(head)) == [5, 4, 2, 3, 1]