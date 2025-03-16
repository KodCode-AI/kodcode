from solution import *

from solution import ListNode, reverse_linked_list

def construct_linked_list(values):
    """Constructs a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def to_list(node):
    """Converts a linked list to a list of values."""
    values = []
    while node:
        values.append(node.value)
        node = node.next
    return values

def test_reverse_linked_list():
    # Test with a non-empty list
    assert to_list(reverse_linked_list(construct_linked_list([1, 2, 3, 4]))) == [4, 3, 2, 1]

    # Test with a single element
    assert to_list(reverse_linked_list(construct_linked_list([5]))) == [5]

    # Test with an empty list
    assert to_list(reverse_linked_list(construct_linked_list([]))) == []

    # Test with a negative number
    assert to_list(reverse_linked_list(construct_linked_list([-5, 6, -7, 8]))) == [8, -7, 6, -5]

    # Test with all negative numbers
    assert to_list(reverse_linked_list(construct_linked_list([-1, -2, -3, -4]))) == [-4, -3, -2, -1]

    # Test with repeated numbers
    assert to_list(reverse_linked_list(construct_linked_list([1, 1, 1, 1]))) == [1, 1, 1, 1]