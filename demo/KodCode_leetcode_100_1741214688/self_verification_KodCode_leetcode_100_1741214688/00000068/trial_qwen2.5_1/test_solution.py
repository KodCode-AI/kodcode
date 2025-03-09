from solution import *

from solution import TreeNode, min_balance_factor

def test_min_balance_factor_empty_tree():
    assert min_balance_factor(None) == 0

def test_min_balance_factor_single_node():
    root = TreeNode(1)
    assert min_balance_factor(root) == 0

def test_min_balance_factor_balanced_tree():
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    assert min_balance_factor(root) == 0

def test_min_balance_factor_skewed_left_tree():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert min_balance_factor(root) == 3

def test_min_balance_factor_skewed_right_tree():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    assert min_balance_factor(root) == 3

def test_min_balance_factor_mixed_tree():
    root = TreeNode(1, TreeNode(2, TreeNode(4, None, TreeNode(5))), TreeNode(3))
    assert min_balance_factor(root) == 1