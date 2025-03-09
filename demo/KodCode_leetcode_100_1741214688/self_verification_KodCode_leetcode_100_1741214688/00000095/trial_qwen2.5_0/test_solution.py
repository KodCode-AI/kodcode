from solution import *

from solution import TreeNode, can_partition_bst, sum_node_values

def test_can_partition_bst_true():
    # Construct a BST with values 1 to 5
    five = TreeNode(5)
    four = TreeNode(4)
    three = TreeNode(3)
    two = TreeNode(2, left=four, right=five)
    one = TreeNode(1, right=three)
    assert can_partition_bst(one) == True

def test_can_partition_bst_false():
    # Construct a BST with values 1, 2, 3
    three = TreeNode(3)
    two = TreeNode(2)
    one = TreeNode(1, right=three, left=two)
    assert can_partition_bst(one) == False

def test_sum_node_values():
    root = TreeNode(5, left=TreeNode(3), right=TreeNode(1))
    assert sum_node_values(root) == 9

def test_can_partition_helper():
    root = TreeNode(5, left=TreeNode(3), right=TreeNode(1))
    assert can_partition_helper(root, 8) == True
    assert can_partition_helper(root, 9) == False