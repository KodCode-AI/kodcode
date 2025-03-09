from solution import *

def create_bst() -> TreeNode:
    """
    Creates and returns a simple BST with nodes 2, 1, and 3.
    """
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    return root

def test_find_in_bst():
    root = create_bst()
    assert find_in_bst(root, 1) == True
    assert find_in_bst(root, 3) == True
    assert find_in_bst(root, 2) == True
    assert find_in_bst(root, 4) == False

def test_insert_into_bst():
    root = create_bst()
    assert find_in_bst(insert_into_bst(root, 4), 4) == True
    assert find_in_bst(insert_into_bst(root, 0), 0) == True
    assert find_in_bst(insert_into_bst(root, -1), -1) == True
    assert find_in_bst(root, 2) == True

def test_insertion_maintains_structure():
    root = create_bst()
    new_root = insert_into_bst(root, 4)
    assert find_in_bst(new_root.left, 1) == True
    assert find_in_bst(new_root.right, 3) == True
    assert find_in_bst(new_root.right.right, 4) == True