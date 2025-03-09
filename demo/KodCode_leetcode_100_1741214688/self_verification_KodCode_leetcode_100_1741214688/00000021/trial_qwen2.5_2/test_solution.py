from solution import *

import pytest

def create_bst(*args):
    """Helper function to create a BST from given arguments."""
    nodes = {val: TreeNode(val) for val in args}
    for i, (val, left, right) in enumerate(zip(args, [args[i + 1] for i in range(len(args) - 1)], [None if i + 2 >= len(args) else args[i + 2] for i in range(len(args) - 1)])):
        nodes[val].left = nodes[left] if left is not None else None
        nodes[val].right = nodes[right] if right is not None else None
    return nodes[args[0]]

def test_kthSmallest():
    root = create_bst(3, 1, 4, 0, 2)
    assert kthSmallest(root, 1) == 0
    assert kthSmallest(root, 2) == 1
    assert kthSmallest(root, 3) == 2
    assert kthSmallest(root, 4) == 3
    assert kthSmallest(root, 5) == 4

def test_kthSmallest_large_tree():
    root = create_bst(5, 3, 7, 2, 4, None, 8, 1, None, None, None, None, 6, None, 9)
    assert kthSmallest(root, 1) == 1
    assert kthSmallest(root, 8) == 7
    assert kthSmallest(root, 9) == 9

def test_kthSmallest_empty_tree():
    assert kthSmallest(None, 1) is None

def test_kthSmallest_single_node_tree():
    root = create_bst(5)
    assert kthSmallest(root, 1) == 5

def test_kthSmallest_out_of_bounds():
    root = create_bst(5)
    assert kthSmallest(root, 2) is None