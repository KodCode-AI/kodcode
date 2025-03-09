from solution import *

import pytest
from solution import sum_numbers, TreeNode

def create_tree(*values):
    """
    Helper function to create a binary tree from a flat list of values,
    where a null node is represented by None.
    """
    if not values:
        return None
    nodes = [None if val is None else TreeNode(val) for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

def test_sum_numbers_single_node():
    assert sum_numbers(create_tree(1)) == 1

def test_sum_numbers_leaf_nodes():
    assert sum_numbers(create_tree(1, 2, 3)) == 25  # 12 + 13 = 25
    assert sum_numbers(create_tree(4, 9, 0, 5, 1)) == 1026  # 490 + 491 = 1026

def test_sum_numbers_with_one_path():
    assert sum_numbers(create_tree(1,2)) == 12

def test_sum_numbers_complex_tree():
    assert sum_numbers(create_tree(1,2,3,4,5,6,7,8,None,None, None, None, None, None, None, 9)) == 1026 # 123 + 124 + 135 + 136 + 147 + 148 + 159 + 169 = 1026