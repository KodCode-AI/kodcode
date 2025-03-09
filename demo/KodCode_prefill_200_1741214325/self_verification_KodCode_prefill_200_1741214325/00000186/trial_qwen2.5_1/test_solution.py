from solution import *

from solution import ListNode, reverse_linked_list_with_stack

def create_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

def test_reverse_linked_list_with_stack():
    # Test with a simple linked list
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverse_linked_list_with_stack(head)
    assert linked_list_to_list(reversed_head) == [5, 4, 3, 2, 1]
    
    # Test with an empty linked list
    head = create_linked_list([])
    assert linked_list_to_list(reverse_linked_list_with_stack(head)) == []
    
    # Test with a single element linked list
    head = create_linked_list([1])
    assert linked_list_to_list(reverse_linked_list_with_stack(head)) == [1]
    
    # Test with a reversed linked list
    head = create_linked_list([5, 4, 3, 2, 1])
    assert linked_list_to_list(reverse_linked_list_with_stack(head)) == [1, 2, 3, 4, 5]

test_reverse_linked_list_with_stack()