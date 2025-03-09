from solution import *

import pytest

def create_tree(*values):
    """
    Helper function to create a binary tree from a list of values.
    """
    nodes = [TreeNode(val) if val is not None else None for val in values]
    for idx, node in enumerate(nodes):
        if 2 * idx + 1 < len(nodes):
            node.left = nodes[2 * idx + 1]
        if 2 * idx + 2 < len(nodes):
            node.right = nodes[2 * idx + 2]
    return nodes[0]

def test_find_min_balance_factor_empty_tree():
    assert find_min_balance_factor(None) == 0

def test_find_min_balance_factor_balanced_tree():
    root = create_tree(1, 2, 3, 4)
    assert find_min_balance_factor(root) == 0

def test_find_min_balance_factor_unbalanced_tree():
    root = create_tree(1, 2, 3, None, 4)
    assert find_min_balance_factor(root) == 0

def test_find_min_balance_factor_complex_tree():
    root = create_tree(1, 2, 3, 4, 5)
    assert find_min_balance_factor(root) == 1

def test_find_min_balance_factor_single_node():
    root = create_tree(1)
    assert find_min_balance_factor(root) == 0