from solution import *

import pytest
from solution import mirror_tree, TreeNode

def test_mirror_tree_simple():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    mirrored_root = mirror_tree(root)
    assert mirrored_root.left.val == 3
    assert mirrored_root.right.val == 2

def test_mirror_tree_complex():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    mirrored_root = mirror_tree(root)
    assert mirrored_root.left.val == 3
    assert mirrored_root.right.val == 2
    assert mirrored_root.right.left.val == 5
    assert mirrored_root.right.right.val == 4

def test_mirror_tree_single_node():
    root = TreeNode(1)
    mirrored_root = mirror_tree(root)
    assert mirrored_root == root

def test_mirror_tree_empty():
    mirrored_root = mirror_tree(None)
    assert mirrored_root is None