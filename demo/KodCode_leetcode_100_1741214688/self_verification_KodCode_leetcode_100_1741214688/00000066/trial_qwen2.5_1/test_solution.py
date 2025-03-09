from solution import *

from typing import List
from solution import count_valid_sequences

def build_bst(from_list: List[int]) -> TreeNode:
    if not from_list:
        return None
    import math
    def build_tree(nodes: List[TreeNode], index: int) -> TreeNode:
        if index < len(nodes) and nodes[index]:
            node = nodes[index]
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            node.left = build_tree(nodes, left_index)
            node.right = build_tree(nodes, right_index)
            return node
    nodes = [TreeNode(val) if val is not None else None for val in from_list]
    return build_tree(nodes, 0)

# Test case
def test_count_valid_sequences():
    root = build_bst([5, 3, 7, 2, 4])
    assert count_valid_sequences(root) == 3

def test_count_valid_sequences_with Repeat():
    # This tree doesn't have the increasing/decreasing subsequence property
    root = build_bst([8, 5, 9, 4, 7, 10, 11])
    assert count_valid_sequences(root) == 0

def test_count_valid_sequences_with_only_leaf():
    root = build_bst([1])
    assert count_valid_sequences(root) == 1