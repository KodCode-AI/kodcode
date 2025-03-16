from solution import *

import pytest
from solution import diameter_of_binary_tree, TreeNode

# Helper function to create a binary tree
def create_tree(arr: list) -> TreeNode:
    if not arr:
        return None
    nodes = [None if val is None else TreeNode(val) for val in arr]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

def test_diameter_of_binary_tree_example1():
    tree = create_tree([1, 2, 3, 4, 5])
    assert diameter_of_binary_tree(tree) == 3

def test_diameter_of_binary_tree_example2():
    tree = create_tree([1, 2, 3, 4, None, 5])
    assert diameter_of_binary_tree(tree) == 4

def test_diameter_of_binary_tree_single_node():
    tree = create_tree([1])
    assert diameter_of_binary_tree(tree) == 0

def test_diameter_of_binary_tree_empty_tree():
    tree = None
    assert diameter_of_binary_tree(tree) == 0

def test_diameter_of_binary_tree_max_depth():
    tree = create_tree([1, 2, 3, None, 4, 5, 6, 7, 8, 9])
    assert diameter_of_binary_tree(tree) == 6

def test_diameter_of_binary_tree_unbalanced_tree():
    tree = create_tree([1, 2, 3, 4, 5, None, 7])
    assert diameter_of_binary_tree(tree) == 4