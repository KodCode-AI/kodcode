from solution import *

from solution import findClosestLeaf

def test_closest_leaf_negative():
    # Constructing a BST for the test case
    #         3
    #        / \
    #       1   4
    #          / \
    #         2   5
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4, TreeNode(2), TreeNode(5))

    assert findClosestLeaf(root, 3) == 4
    assert findClosestLeaf(root, 2) == 2
    assert findClosestLeaf(root, 4) == 5

def test_closest_leaf_edge_cases():
    # Empty tree case
    assert findClosestLeaf(None, 3) is None
    # One node tree case
    root = TreeNode(3)
    assert findClosestLeaf(root, 3) == 3

def test_closest_leaf_positive():
    # Constructing a BST for the test case
    #          1
    #           \
    #            2
    #             \
    #              3
    root = TreeNode(1, right=TreeNode(2, right=TreeNode(3)))

    assert findClosestLeaf(root, 1) == 3
    assert findClosestLeaf(root, 3) == 3

def test_closest_leaf_multiple_targets():
    # Constructing a BST for the test case
    #         5
    #        / \
    #       3   6
    #      / \ / \
    #     2  4 7  8
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, TreeNode(7), TreeNode(8)))

    assert findClosestLeaf(root, 6) in [7, 8]