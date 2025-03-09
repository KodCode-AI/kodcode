from solution import *

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_duplicate_linked_list():
    # Test with a simple linked list: 1 -> 2 -> 3
    head = create_linked_list([1, 2, 3])
    copied_head = duplicate_linked_list(head)
    assert linked_list_to_list(copied_head) == [1, 2, 3]
    
    # Test with an empty linked list
    head = create_linked_list([])
    copied_head = duplicate_linked_list(head)
    assert linked_list_to_list(copied_head) == []
    
    # Test with a linked list with one element: 4
    head = create_linked_list([4])
    copied_head = duplicate_linked_list(head)
    assert linked_list_to_list(copied_head) == [4]
    
    # Test with a more complex linked list: 10 -> 20 -> 30 -> 40 -> 50
    head = create_linked_list([10, 20, 30, 40, 50])
    copied_head = duplicate_linked_list(head)
    assert linked_list_to_list(copied_head) == [10, 20, 30, 40, 50]

test_duplicate_linked_list()