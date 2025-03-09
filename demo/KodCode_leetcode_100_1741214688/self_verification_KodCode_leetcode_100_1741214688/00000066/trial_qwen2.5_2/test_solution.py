from solution import *

import pytest
from typing import *
from solution import TreeNode, count_valid_sequences

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def test_count_valid_sequences_simple():
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7))
    assert count_valid_sequences(root) == 2

def test_count_valid_sequences_empty_tree():
    assert count_valid_sequences(None) == 0

def test_count_valid_sequences_single_node():
    root = TreeNode(5)
    assert count_valid_sequences(root) == 1

def test_count_valid_sequences_root_restricted():
    root = TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(8)), TreeNode(15, TreeNode(13), TreeNode(22)))
    assert count_valid_sequences(root) == 3

def test_count_valid_sequences_large_sequence():
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(10, TreeNode(8, TreeNode(6), TreeNode(9)), TreeNode(12)))
    assert count_valid_sequences(root) == 3