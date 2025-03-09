from solution import *

from solution import max_depth_bst, TreeNode

def setup_tree():
    # Creating a simple BST
    #       3
    #      / \
    #     2   5
    #    /   / \
    #   1   4   6
    root = TreeNode(3)
    root.left = TreeNode(2, left=TreeNode(1))
    root.right = TreeNode(5, left=TreeNode(4), right=TreeNode(6))
    return root

def test_max_depth_bst_empty_tree():
    assert max_depth_bst(None) == 0

def test_max_depth_bst_simple_tree():
    root = setup_tree()
    assert max_depth_bst(root) == 3

def test_max_depth_bst_with_deeper_right():
    #       3
    #      /
    #     2
    #    / \
    #   1   5
    #      / \
    #     4   6
    root = TreeNode(3)
    root.left = TreeNode(2, left=TreeNode(1))
    root.right = TreeNode(5, left=TreeNode(4), right=TreeNode(6))
    assert max_depth_bst(root) == 4