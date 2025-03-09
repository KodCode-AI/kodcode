from solution import *

from solution import TreeNode, sum_of_left_leaves

def test_sum_of_left_leaves_empty_tree():
    assert sum_of_left_leaves(None) == 0

def test_sum_of_left_leaves_no_left_leaves():
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert sum_of_left_leaves(root) == 0

def test_sum_of_left_leaves_left_leaf_only():
    root = TreeNode(3)
    root.left = TreeNode(9)
    assert sum_of_left_leaves(root) == 9

def test_sum_of_left_leaves_right_leaf():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    assert sum_of_left_leaves(root) == 9

def test_sum_of_left_leaves_complex_tree():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.left.left = TreeNode(4)
    assert sum_of_left_leaves(root) == 13