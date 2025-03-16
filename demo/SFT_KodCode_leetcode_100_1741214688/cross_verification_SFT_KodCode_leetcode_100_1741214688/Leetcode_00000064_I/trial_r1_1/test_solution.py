from solution import *

from solution import TreeNode, find_in_bst, insert_in_bst

def test_find_in_bst():
    # Create a simple BST
    root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, None, TreeNode(7))), TreeNode(10, None, TreeNode(14)))
    assert find_in_bst(root, 3) == True
    assert find_in_bst(root, 10) == True
    assert find_in_bst(root, 5) == False

def test_insert_in_bst():
    # Create a simple tree and insert nodes
    root = TreeNode(8)
    insert_in_bst(root, 3)
    insert_in_bst(root, 10)
    assert find_in_bst(root, 3) == True
    assert find_in_bst(root, 10) == True

def test_insertion_multiple_nodes():
    root = TreeNode(8)
    insert_in_bst(root, 3)
    insert_in_bst(root, 10)
    insert_in_bst(root, 1)
    assert find_in_bst(root, 3) == True
    assert find_in_bst(root, 10) == True
    assert find_in_bst(root, 1) == True
    assert find_in_bst(root, 14) == False  # Before insertion
    insert_in_bst(root, 14)
    assert find_in_bst(root, 14) == True