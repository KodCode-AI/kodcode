from solution import *

def create_tree():
    """
    Helper function to create a sample BST.
    """
    tree = TreeNode(10)
    tree.left = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(7))
    tree.right = TreeNode(15, None, TreeNode(18))
    return tree

def test_rangeSumBST():
    root = create_tree()
    assert rangeSumBST(root, 7, 15) == 32
    assert rangeSumBST(root, 11, 14) == 0
    assert rangeSumBST(root, 1, 10) == 22
    assert rangeSumBST(root, 5, 20) == 69
    assert rangeSumBST(root, -100, 100) == 69  # This tests if values outside the range are not counted.

def test_empty_tree():
    assert rangeSumBST(None, 7, 15) == 0