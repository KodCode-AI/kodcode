from solution import *

def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(node):
    """Helper function to convert a linked list back to a list of values."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_duplicate_linked_list():
    # Test with empty list
    assert linked_list_to_list(duplicate_linked_list(None)) == []
    
    # Test with a simple linked list: 1 -> 2 -> 3
    original_list = create_linked_list([1, 2, 3])
    duplicated_list = duplicate_linked_list(original_list)
    assert linked_list_to_list(duplicated_list) == [1, 2, 3]
    
    # Test with a more complex linked list
    original_list = create_linked_list([1, 2, 3, 4, 5])
    duplicated_list = duplicate_linked_list(original_list)
    assert linked_list_to_list(duplicated_list) == [1, 2, 3, 4, 5]

# Run the tests
test_duplicate_linked_list()