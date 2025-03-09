from solution import *

from solution import ListNode, reverse_linked_list

def test_reverse_linked_list():
    # Create a linked list 1 -> 2 -> 3
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    
    # Reverse it to 3 -> 2 -> 1
    reversed_head = reverse_linked_list(node1)
    assert reversed_head.value == 3
    
    # Check the next nodes
    assert reversed_head.next.value == 2
    assert reversed_head.next.next.value == 1
    
def test_reverse_empty_list():
    # Reverse an empty list, should return None
    assert reverse_linked_list(None) is None

def test_reverse_single_node():
    # Reverse a single node list, should return the same node
    node = ListNode(4)
    assert reverse_linked_list(node).value == 4