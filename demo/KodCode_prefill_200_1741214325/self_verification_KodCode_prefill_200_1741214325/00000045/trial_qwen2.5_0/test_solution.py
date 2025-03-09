from solution import *

import pytest

# Helper function to create linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list of values
def linked_list_to_list(node):
    values = []
    while node:
        values.append(node.value)
        node = node.next
    return values

def test_duplicate_linked_list_empty_list():
    assert linked_list_to_list(duplicate_linked_list(None)) == []

def test_duplicate_linked_list_simple_list():
    head = create_linked_list([1, 2, 3])
    duplicated_head = duplicate_linked_list(head)
    assert linked_list_to_list(duplicated_head) == [1, 2, 3]

def test_duplicate_linked_list_complex_list():
    head = create_linked_list([1, 2, 3, 4, 5])
    duplicated_head = duplicate_linked_list(head)
    assert linked_list_to_list(duplicated_head) == [1, 2, 3, 4, 5]

def test_duplicate_linked_list_same_elements():
    head = create_linked_list([1, 1, 1, 1])
    duplicated_head = duplicate_linked_list(head)
    assert linked_list_to_list(duplicated_head) == [1, 1, 1, 1]

def test_duplicate_linked_list_with_none():
    head = create_linked_list([None, 1, None, 2])
    duplicated_head = duplicate_linked_list(head)
    assert linked_list_to_list(duplicated_head) == [None, 1, None, 2]