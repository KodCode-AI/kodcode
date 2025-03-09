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
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return values

def test_reverse_linked_list():
    assert linked_list_to_list(reverse_linked_list(None)) == []
    assert linked_list_to_list(reverse_linked_list(create_linked_list([1]))) == [1]
    assert linked_list_to_list(reverse_linked_list(create_linked_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert linked_list_to_list(reverse_linked_list(create_linked_list([1, 3, 5, 7, 9]))) == [9, 7, 5, 3, 1]

import pytest
@pytest.mark.parametrize("values, expected", [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 3, 5, 7, 9], [9, 7, 5, 3, 1])
])
def test_reverse_linked_list_parametrized(values, expected):
    head = create_linked_list(values)
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == expected