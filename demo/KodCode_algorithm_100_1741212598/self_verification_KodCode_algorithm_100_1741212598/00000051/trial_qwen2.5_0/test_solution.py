from solution import *

import pytest

def test_enhanced_inorder_traversal():
    class BinaryTreeNode:
        def __init__(self, data: int) -> None:
            self.data = data
            self.left_child: Optional[BinaryTreeNode] = None
            self.right_child: Optional[BinaryTreeNode] = None

    def make_tree() -> BinaryTreeNode:
        root = BinaryTreeNode(15)
        root.left_child = BinaryTreeNode(10)
        root.right_child = BinaryTreeNode(25)
        root.left_child.left_child = BinaryTreeNode(6)
        root.left_child.right_child = BinaryTreeNode(14)
        root.right_child.left_child = BinaryTreeNode(20)
        root.right_child.right_child = BinaryTreeNode(60)
        return root

    result = enhanced_inorder_traversal(make_tree())
    expected = [6, 10, 14, 15, 20, 25, 60]
    assert result == expected, "The result does not match the expected output."

def test_enhanced_inorder_traversal_empty_tree():
    result = enhanced_inorder_traversal(None)
    expected = []
    assert result == expected, "The result does not match the expected output for an empty tree."

def test_enhanced_inorder_traversal_single_node():
    root = BinaryTreeNode(10)
    result = enhanced_inorder_traversal(root)
    expected = [10]
    assert result == expected, "The result does not match the expected output for a single node tree."

def test_enhanced_inorder_traversal_deeper_tree():
    class BinaryTreeNode:
        def __init__(self, data: int) -> None:
            self.data = data
            self.left_child: Optional[BinaryTreeNode] = None
            self.right_child: Optional[BinaryTreeNode] = None

    def make_deep_tree() -> BinaryTreeNode:
        root = BinaryTreeNode(15)
        root.left_child = BinaryTreeNode(10)
        for i in range(50, 90, 10):  # Add nodes from 50 to 80 in steps of 10
            current = root.left_child
            while current.right_child:
                current = current.right_child
            current.right_child = BinaryTreeNode(i)
        return root

    result = enhanced_inorder_traversal(make_deep_tree())
    expected = [50, 60, 70, 80, 90, 10, 15]
    assert result == expected, "The result does not match the expected output for a deeper tree."