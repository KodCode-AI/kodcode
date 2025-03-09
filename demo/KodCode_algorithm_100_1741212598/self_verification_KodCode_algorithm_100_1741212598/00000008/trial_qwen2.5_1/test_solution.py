from solution import *

def test_detect_cycle_with_cycle():
    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    linked_list.add_node(4)

    # Create a cycle in the linked list
    linked_list.head.next_node.next_node.next_node = linked_list.head.next_node

    assert detect_cycle(linked_list) == True

def test_detect_cycle_without_cycle():
    linked_list2 = LinkedList()
    linked_list2.add_node(1)

    assert detect_cycle(linked_list2) == False

def test_detect_cycle_empty_list():
    assert detect_cycle(LinkedList()) == False

def test_detect_cycle_single_node_list():
    assert detect_cycle(LinkedList()) == False
    linked_list = LinkedList()
    linked_list.head = Node(1)
    assert detect_cycle(linked_list) == False