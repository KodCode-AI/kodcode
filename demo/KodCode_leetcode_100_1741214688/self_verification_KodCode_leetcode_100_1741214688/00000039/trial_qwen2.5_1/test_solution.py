from solution import *

import pytest
from solution import rangeSumBST  # Assuming the solution is saved in a file named 'solution.py'

def create_bst_from_list(values, root=None, i=0):
    if i < len(values):
        if values[i] is None:
            return None
        node = TreeNode(values[i])
        node.left = create_bst_from_list(values, root, 2 * i + 1)
        node.right = create_bst_from_list(values, root, 2 * i + 2)
        return node

def test_range_sum_bst():
    # Construct a BST: 
    #       10
    #      /  \
    #     5   15
    #    / \    \
    #   3   7    18
    bst = create_bst_from_list([10, 5, 15, 3, 7, None, 18])
    assert rangeSumBST(bst, 7, 15) == 32

def test_range_sum_empty_tree():
    assert rangeSumBST(None, 7, 15) == 0

def test_range_sum_single_node_tree():
    node = TreeNode(10)
    assert rangeSumBST(node, 7, 15) == 10

def test_range_sum_no_nodes_in_range():
    bst = create_bst_from_list([10, 5, 15, 3, 7, None, 18])
    assert rangeSumBST(bst, 20, 25) == 0

def test_range_sum_all_nodes_in_range():
    bst = create_bst_from_list([10, 5, 15, 3, 7, None, 18])
    assert rangeSumBST(bst, 0, 20) == 63