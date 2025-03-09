from solution import *

``
from solution import TreeNode, max_depth_bst

def test_max_depth_bst_empty_tree():
    assert max_depth_bst(None) == 0

def test_max_depth_bst_single_node():
    root = TreeNode(5)
    assert max_depth_bst(root) == 1

def test_max_depth_bst_balanced_tree():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    assert max_depth_bst(root) == 3

def test_max_depth_bst_skewed_right():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert max_depth_bst(root) == 3

def test_max_depth_bst_skewed_left():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert max_depth_bst(root) == 3