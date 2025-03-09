from solution import *

from solution import TreeNode, vertical_order

def test_vertical_order_example():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    expected = [[9], [3, 15], [20], [7]]
    assert vertical_order(root) == expected

def test_vertical_order_single_node():
    root = TreeNode(1)
    expected = [[1]]
    assert vertical_order(root) == expected

def test_vertical_order_empty_tree():
    assert vertical_order(None) == []

def test_vertical_order.empty_space_in_tree():
    root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
    expected = [[2], [1, 3], [4]]
    assert vertical_order(root) == expected

def test_vertical_order_multiple_levels():
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    expected = [[4], [2], [1, 3, 5]]
    assert vertical_order(root) == expected