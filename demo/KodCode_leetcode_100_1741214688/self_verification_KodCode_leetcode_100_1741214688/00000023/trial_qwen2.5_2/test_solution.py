from solution import *

import pytest
from solution import TreeNode, findClosestLeaf

@pytest.fixture
def binary_search_tree():
    """
    Fixture to create a simple binary search tree for testing.
    """
    node10 = TreeNode(10)
    node5 = TreeNode(5)
    node15 = TreeNode(15)
    node3 = TreeNode(3)
    node7 = TreeNode(7)
    node14 = TreeNode(14)
    node20 = TreeNode(20)
    
    node15.left = node14
    node15.right = node20
    node10.left = node5
    node10.right = node15
    node5.left = node3
    node5.right = node7
    node7.left = node14
    
    return node10

def test_find_closest_leaf_root_node(binary_search_tree):
    assert findClosestLeaf(binary_search_tree, 10) == 7

def test_find_closest_leaf_leaf_node(binary_search_tree):
    assert findClosestLeaf(binary_search_tree, 3) == 3

def test_find_closest_leaf_target_in_between(binary_search_tree):
    assert findClosestLeaf(binary_search_tree, 11) in [7, 14]  # Both nodes are at the same distance

def test_find_closest_leaf_target_not_found():
    with pytest.raises(AssertionError):
        findClosestLeaf(None, 10)

def test_find_closest_leaf_distance_from_leaf(binary_search_tree):
    assert findClosestLeaf(binary_search_tree, 14) in [7, 15]  # Both nodes are at the same distance

def test_find_closest_leaf_multi_edges(binary_search_tree):
    node8 = TreeNode(8, left=TreeNode(4, left=TreeNode(1, left=TreeNode(0))), right=TreeNode(9, right=TreeNode(10)))
    assert findClosestLeaf(node8, 0) == 1