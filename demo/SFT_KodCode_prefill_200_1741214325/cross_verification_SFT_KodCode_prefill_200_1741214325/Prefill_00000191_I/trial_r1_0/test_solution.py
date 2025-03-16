from solution import *

from solution import ListNode, reverse_linked_list

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
        result.append(current.value)
        current = current.next
    return result

def test_reverse_linked_list():
    assert linked_list_to_list(reverse_linked_list(None)) == []
    assert linked_list_to_list(reverse_linked_list(create_linked_list([1]))) == [1]
    assert linked_list_to_list(reverse_linked_list(create_linked_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert linked_list_to_list(reverse_linked_list(create_linked_list([1, 2]))) == [2, 1]