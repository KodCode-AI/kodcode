from solution import *

from solution import max_depth_bst, TreeNode

def test_max_depth_bst_empty_tree():
    assert max_depth_bst(None) == 0

def test_max_depth_bst_single_node():
    root = TreeNode(1)
    assert max_depth_bst(root) == 1

def test_max_depth_bst_balanced_tree():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert max_depth_bst(root) == 2

def test_max_depth_bst_unbalanced_tree_left():
    root = TreeNode(2, TreeNode(1, TreeNode(0), None), TreeNode(3))
    assert max_depth_bst(root) == 3

def test_max_depth_bst_unbalanced_tree_right():
    root = TreeNode(2, TreeNode(1), TreeNode(3, None, TreeNode(4)))
    assert max_depth_bst(root) == 3