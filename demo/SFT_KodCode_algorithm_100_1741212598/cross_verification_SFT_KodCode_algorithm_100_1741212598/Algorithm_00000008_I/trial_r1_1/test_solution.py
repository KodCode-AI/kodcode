from solution import *

from solution import Node, LinkedList, detect_cycle

def test_detect_cycle_with_cycle():
    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    linked_list.add_node(4)

    # Create a cycle in the linked list
    linked_list.head.next_node.next_node.next_node = linked_list.head.next_node

    assert detect_cycle(linked_list) == True

def test_detect_cycle_with_no_cycle_one_node():
    linked_list = LinkedList()
    linked_list.add_node(1)

    assert detect_cycle(linked_list) == False

def test_detect_cycle_with_no_cycle_two_nodes():
    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.head.next_node.next_node = None  # Break the cycle

    assert detect_cycle(linked_list) == False

def test_detect_cycle_empty_list():
    linked_list = LinkedList()

    assert detect_cycle(linked_list) == False

def test_detect_cycle_with_cycle_in_middle():
    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    linked_list.add_node(4)
    linked_list.head.next_node.next_node.next_node.next_node = linked_list.head.next_node

    assert detect_cycle(linked_list) == True

def test_detect_cycle_with_cycle_at_end():
    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    linked_list.add_node(4)
    linked_list.head.next_node.next_node.next_node.next_node = linked_list.head.next_node

    assert detect_cycle(linked_list) == True