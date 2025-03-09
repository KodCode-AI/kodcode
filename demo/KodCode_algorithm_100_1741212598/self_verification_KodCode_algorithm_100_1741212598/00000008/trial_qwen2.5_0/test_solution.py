from solution import *

import pytest

class TestDetectCycle:
    def setup_method(self):
        self.empty_list = LinkedList()
        self.single_node_list = LinkedList()
        self.single_node_list.add_node(1)
        self.cycle_list = LinkedList()
        self.cycle_list.add_node(1)
        self.cycle_list.add_node(2)
        self.cycle_list.add_node(3)
        self.cycle_list.add_node(4)
        self.cycle_list.head.next_node.next_node.next_node = self.cycle_list.head.next_node

    def test_empty_list(self):
        assert detect_cycle(self.empty_list) == False

    def test_single_node_list(self):
        assert detect_cycle(self.single_node_list) == False

    def test_cycle_list(self):
        assert detect_cycle(self.cycle_list) == True

    def test_no_cycle_list(self):
        no_cycle_list = LinkedList()
        no_cycle_list.add_node(1)
        no_cycle_list.add_node(2)
        no_cycle_list.add_node(3)
        no_cycle_list.add_node(4)
        no_cycle_list.add_node(5)
        assert detect_cycle(no_cycle_list) == False