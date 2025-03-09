from solution import *

import pytest
from solution import max_depth, TreeNode

def create_tree(*values):
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

def test_max_depth_empty_tree():
    assert max_depth(None) == 0

def test_max_depth_single_node():
    node = TreeNode(1)
    assert max_depth(node) == 1

def test_max_depth_balanced_tree():
    root = create_tree(3, 9, 20, None, None, 15, 7)
    assert max_depth(root) == 3

def test_max_depth_right_heavy_tree():
    root = create_tree(1, None, 2, None, 3, None, 4)
    assert max_depth(root) == 4

def test_max_depth_left_heavy_tree():
    root = create_tree(1, 2, None, 3, 4, None, None)
    assert max_depth(root) == 4