from solution import *

import pytest

# Mock TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(*values):
    nodes = [TreeNode(v) if v is not None else None for v in values]
    for i in range(len(nodes) // 2):
        if nodes[i] is not None:
            nodes[i].left = nodes[2 * i + 1] if 2 * i + 1 < len(nodes) else None
            nodes[i].right = nodes[2 * i + 2] if 2 * i + 2 < len(nodes) else None
    return nodes[0]

def sum_numbers(root):
    """
    Returns the sum of all root-to-leaf numbers in the binary tree.
    """
    return _sum_numbers(root, 0)

def _sum_numbers(node, current_number):
    if not node:
        return 0
    current_number = current_number * 10 + node.val
    if not node.left and not node.right:  # It's a leaf node
        return current_number
    return _sum_numbers(node.left, current_number) + _sum_numbers(node.right, current_number)

def test_sum_numbers():
    assert sum_numbers(create_tree(1, 2, 3)) == 25  # 1->2 and 1->3, 25 = 12 + 13
    assert sum_numbers(create_tree(4, 9, 0, 5, 1)) == 408  # 4->9->5 and 4->9->0->1, 408 = 495 + 4901

def test_single_node():
    assert sum_numbers(create_tree(1)) == 1  # The tree consists of a single node 1

def test_empty_tree():
    assert sum_numbers(None) == 0  # An empty tree

def test_no_leaf_nodes():
    assert sum_numbers(create_tree(1, 2)) == 12  # 1 and 2, but no path to a leaf node, so only 12