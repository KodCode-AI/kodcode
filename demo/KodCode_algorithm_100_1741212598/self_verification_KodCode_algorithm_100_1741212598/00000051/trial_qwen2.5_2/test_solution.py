from solution import *

import pytest
from solution import BinaryTreeNode, enhanced_inorder_traversal, make_tree

def test_enhanced_inorder_traversal_with_example():
    tree = make_tree()
    result = enhanced_inorder_traversal(tree)
    expected = [6, 10, 14, 15, 20, 25, 60]
    assert result == expected, "The result does not match the expected output."

def test_enhanced_inorder_traversal_with_empty_tree():
    result = enhanced_inorder_traversal(None)
    expected = []
    assert result == expected, "The result does not match the expected output for an empty tree."

def test_enhanced_inorder_traversal_with_single_node():
    root = BinaryTreeNode(15)
    result = enhanced_inorder_traversal(root)
    expected = [15]
    assert result == expected, "The result does not match the expected output for a single node tree."

def test_enhanced_inorder_traversal_with_deeper_left_subtree():
    root = BinaryTreeNode(1)
    root.left_child = BinaryTreeNode(2)
    root.left_child.left_child = BinaryTreeNode(3)
    root.left_child.left_child.left_child = BinaryTreeNode(4)
    result = enhanced_inorder_traversal(root)
    expected = [4, 3, 2, 1]
    assert result == expected, "The result does not match the expected output for a deeper left subtree."

def test_enhanced_inorder_traversal_with_deeper_right_subtree():
    root = BinaryTreeNode(1)
    root.right_child = BinaryTreeNode(2)
    root.right_child.right_child = BinaryTreeNode(3)
    root.right_child.right_child.right_child = BinaryTreeNode(4)
    result = enhanced_inorder_traversal(root)
    expected = [1, 2, 3, 4]
    assert result == expected, "The result does not match the expected output for a deeper right subtree."

def test_enhanced_inorder_traversal_with_non_balanced_tree():
    root = BinaryTreeNode(10)
    root.left_child = BinaryTreeNode(5)
    root.right_child = BinaryTreeNode(15)
    root.left_child.left_child = BinaryTreeNode(3)
    root.left_child.right_child = BinaryTreeNode(7)
    root.right_child.left_child = BinaryTreeNode(12)
    root.right_child.right_child = BinaryTreeNode(18)
    result = enhanced_inorder_traversal(root)
    expected = [3, 5, 7, 10, 12, 15, 18]
    assert result == expected, "The result does not match the expected output for a non-balanced tree."