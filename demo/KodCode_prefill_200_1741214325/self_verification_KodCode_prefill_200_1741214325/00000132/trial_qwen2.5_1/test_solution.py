from solution import *

from solution import diameter_of_binary_tree, TreeNode

def test_diameter_of_binary_tree():
    # Constructing a tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    assert diameter_of_binary_tree(root) == 3

    # Constructing another tree
    #          1
    #         /
    #        2
    #       /
    #      3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    
    assert diameter_of_binary_tree(root) == 3

    # Single node tree
    root = TreeNode(1)
    assert diameter_of_binary_tree(root) == 0

    # Empty tree
    assert diameter_of_binary_tree(None) == 0