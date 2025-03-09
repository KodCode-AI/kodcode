from solution import *

from solution import can_partition_bst, TreeNode

def create_bst():
    """
    Helper function to create a binary search tree for test cases.
    """
    node5 = TreeNode(5)
    node3 = TreeNode(3)
    node7 = TreeNode(7)
    node2 = TreeNode(2, left=TreeNode(1))
    node4 = TreeNode(4, right=TreeNode(3))
    node5.left = node3
    node5.right = node7
    node3.left = node2
    node3.right = node4
    return node5

def test_can_partition_bst_single_element():
    assert can_partition_bst(TreeNode(2)) == False

def test_can_partition_bst_even_sum():
    root = create_bst()
    assert can_partition_bst(root) == True

def test_can_partition_bst_odd_sum():
    node10 = TreeNode(10)
    node8 = TreeNode(8)
    node12 = TreeNode(12)
    node6 = TreeNode(6)
    node10.left = node8
    node10.right = node12
    node8.left = node6
    assert can_partition_bst(node10) == False

def test_can_partition_bst_complex():
    node16 = TreeNode(16)
    node9 = TreeNode(9)
    node21 = TreeNode(21)
    node3 = TreeNode(3)
    node21.left = node16
    node9.right = node21
    node21.right = node3
    assert can_partition_bst(node9) == True