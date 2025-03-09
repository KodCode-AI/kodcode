from solution import *

def create_tree():
    # Creating a tree:
    #     5
    #    / \
    #   3   7
    #  / \
    # 2   4
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    return root

def test_valid_sequences():
    root = create_tree()
    assert count_valid_sequences(root) == 2

def test_invalid_sequences():
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    assert count_valid_sequences(root) == 0

def test_single_node():
    root = TreeNode(5)
    assert count_valid_sequences(root) == 1

def test_no_leaf():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    assert count_valid_sequences(root) == 1

def test_empty_tree():
    assert count_valid_sequences(None) == 0