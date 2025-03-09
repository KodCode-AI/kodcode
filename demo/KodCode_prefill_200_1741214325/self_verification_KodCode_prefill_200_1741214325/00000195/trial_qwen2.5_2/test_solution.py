from solution import *

import pytest
from solution import TreeNode, mirror_tree

# Helper function to create a binary tree from pre-order traversal
def create_tree(preorder):
    root = None
    for value in preorder:
        if root is None:
            root = TreeNode(value)
        else:
            root.insert(value)
    return root

# Helper function to get the in-order traversal of a tree
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.key] + inorder_traversal(root.right)

def test_mirror_tree_simple():
    preorder = [1, 2, 4, 5, 3, 6, 7]
    root = create_tree(preorder)
    mirrored_root = mirror_tree(root)
    expected_inorder = [4, 2, 5, 1, 6, 3, 7]
    assert inorder_traversal(mirrored_root) == expected_inorder

def test_mirror_tree_empty_tree():
    root = None
    mirrored_root = mirror_tree(root)
    assert mirrored_root is None

def test_mirror_tree_single_node():
    root = TreeNode(1)
    mirrored_root = mirror_tree(root)
    assert mirrored_root.key == 1 and mirrored_root.left is None and mirrored_root.right is None

def test_mirror_tree_complex():
    preorder = [10, 20, 15, 30, 35, 40]
    root = create_tree(preorder)
    mirrored_root = mirror_tree(root)
    expected_inorder = [15, 30, 35, 20, 40, 10]
    assert inorder_traversal(mirrored_root) == expected_inorder