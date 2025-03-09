from solution import *

import pytest
from typing import List

def create_tree(nodes: List[TreeNode or None], i: int) -> TreeNode or None:
    if i >= len(nodes) or not nodes[i]:
        return None
    result = TreeNode(nodes[i])
    result.left = create_tree(nodes, 2 * i + 1)
    result.right = create_tree(nodes, 2 * i + 2)
    return result

def to_list(node: TreeNode) -> List[TreeNode or None]:
    if not node:
        return []
    result = [node.val]
    result += to_list(node.left) + to_list(node.right)
    return result

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def test_sum_left_leaves():
    assert sum_left_leaves(create_tree([3,9,20,None,None,15,7], 0)) == 24
    assert sum_left_leaves(create_tree([1,2,3,4], 0)) == 6
    assert sum_left_leaves(create_tree([1,2,3,None,5], 0)) == 5
    assert sum_left_leaves(create_tree([], 0)) == 0

def test_sum_left_leaves_edge_cases():
    assert sum_left_leaves(create_tree([1], 0)) == 0
    assert sum_left_leaves(create_tree([1,2], 0)) == 2
    assert sum_left_leaves(create_tree([1,None,2], 0)) == 0
    assert sum_left_leaves(create_tree([1,None,3,4], 0)) == 4