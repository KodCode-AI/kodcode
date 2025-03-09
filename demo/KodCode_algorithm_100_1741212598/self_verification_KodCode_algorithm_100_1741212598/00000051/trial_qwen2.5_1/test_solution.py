from solution import *

import pytest

class BinaryTreeNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left_child: BinaryTreeNode | None = None
        self.right_child: BinaryTreeNode | None = None

def make_tree() -> BinaryTreeNode | None:
    root = BinaryTreeNode(15)
    root.left_child = BinaryTreeNode(10)
    root.right_child = BinaryTreeNode(25)
    root.left_child.left_child = BinaryTreeNode(6)
    root.left_child.right_child = BinaryTreeNode(14)
    root.right_child.left_child = BinaryTreeNode(20)
    root.right_child.right_child = BinaryTreeNode(60)
    return root

def enhanced_inorder_traversal(root: BinaryTreeNode | None) -> List[int]:
    """
    Performs an inorder traversal on a given BST and returns the values in sorted order.
    """
    if not root:
        return []
    
    stack, result = [], []
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left_child
        
        current = stack.pop()
        result.append(current.data)
        current = current.right_child
    
    return result

def test_enhanced_inorder_traversal_single_node():
    root = BinaryTreeNode(10)
    assert enhanced_inorder_traversal(root) == [10]

def test_enhanced_inorder_traversal_empty_tree():
    assert enhanced_inorder_traversal(None) == []

def test_enhanced_inorder_traversal_balanced_tree():
    tree = make_tree()
    assert enhanced_inorder_traversal(tree) == [6, 10, 14, 15, 20, 25, 60]

def test_enhanced_inorder_traversal_degenerate_tree():
    root = BinaryTreeNode(15)
    root.left_child = BinaryTreeNode(10)
    root.right_child = BinaryTreeNode(25)
    assert enhanced_inorder_traversal(root) == [10, 15, 25]

def test_enhanced_inorder_traversal_negative_numbers():
    root = BinaryTreeNode(-10)
    root.left_child = BinaryTreeNode(-20)
    root.right_child = BinaryTreeNode(-5)
    root.left_child.left_child = BinaryTreeNode(-30)
    root.left_child.right_child = BinaryTreeNode(-15)
    assert enhanced_inorder_traversal(root) == [-30, -20, -15, -10, -5]