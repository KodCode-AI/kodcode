from solution import *

import pytest

def create_tree(*vals):
    nodes = [TreeNode(val=val) for val in vals]
    for i in range(len(nodes)//2):
        if 2*i+1 < len(nodes):
            nodes[i].left = nodes[2*i+1]
        if 2*i+2 < len(nodes):
            nodes[i].right = nodes[2*i+2]
    return nodes[0]

@pytest.fixture
def setup_bst():
    root = create_tree(1, 2, 3, 4, 5)
    root.left.right = TreeNode(val=6)
    root.right.left = TreeNode(val=7)
    return root

def test_findClosestLeaf(setup_bst):
    assert findClosestLeaf(setup_bst, 4) in [4, 3]  # 4 and 3 are both 1 step away

def test_findClosestLeaf_target_closest_setup_bst():
    assert findClosestLeaf(create_tree(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 8) == 7  # 7 is 1 step away

def test_findClosestLeaf_multiple_clicked_leaves():
    assert findClosestLeaf(create_tree(1, 2, 3), 3) == 3  # Node 3 is a leaf itself

def test_findClosestLeaf_empty_tree():
    assert findClosestLeaf(None, 0) == None  # Should return None if tree is empty

def test_findClosestLeaf_root_is_target(setup_bst):
    assert findClosestLeaf(setup_bst, 1) == 1  # 1 is a leaf itself


The provided unit tests cover a variety of scenarios, including multiple leaf nodes, where the root node is the target, and where the tree is empty. The tests ensure that the function behaves as expected in different contexts.