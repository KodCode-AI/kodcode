from solution import *

import pytest
from typing import Optional

# Sample binary search tree nodes setup
def setup_tree():
    """
    Helper function to setup a simple binary search tree.
    Structure:
        10
       /  \
      5    15
     / \   / \
    3   7 13  18
    """
    root = TreeNode(10)
    root.left = TreeNode(5, TreeNode(3), TreeNode(7))
    root.right = TreeNode(15, TreeNode(13), TreeNode(18))
    return root

def test_range_sum_bst_within_range():
    root = setup_tree()
    assert rangeSumBST(root, 7, 15) == 32  # Sum of 7, 10, 13, 15

def test_range_sum_bst_below_low():
    root = setup_tree()
    assert rangeSumBST(root, 16, 20) == 0  # No nodes within that range

def test_range_sum_bst_above_high():
    root = setup_tree()
    assert rangeSumBST(root, 2, 4) == 0  # No nodes within that range

def test_range_sum_bst_single_node_low_to_high():
    root = TreeNode(10)
    assert rangeSumBST(root, 10, 10) == 10  # Only the root node is in the range

def test_range_sum_bst_single_leaf():
    root = TreeNode(10, TreeNode(5), None)
    assert rangeSumBST(root, 5, 15) == 5  # Only the left child node is in the range