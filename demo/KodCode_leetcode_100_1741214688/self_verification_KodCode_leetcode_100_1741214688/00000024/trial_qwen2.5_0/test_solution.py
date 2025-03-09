from solution import *

import pytest
from solution import TreeNode, kthSmallest

def create_bst():
    """
    Helper function to create the BST for testing.
    """
    five = TreeNode(5)
    three = TreeNode(3)
    six = TreeNode(6)
    two = TreeNode(2)
    four = TreeNode(4)
    
    five.left = three
    five.right = six
    three.left = two
    three.right = four
    
    return five

def test_kth_smallest_positive():
    root = create_bst()
    assert kthSmallest(root, 3) == 3
    
def test_kth_smallest_edge_cases():
    root = TreeNode(1)
    assert kthSmallest(root, 1) == 1
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    with pytest.raises(Exception):
        kthSmallest(root, 2)  # This should raise an error as 2nd smallest does not exist

def test_kth_smallest_with_duplicates():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    
    assert kthSmallest(root, 2) == 2

def test_kth_smallest_in_order_traversal():
    root = create_bst()
    assert kthSmallest(root, 4) == 5