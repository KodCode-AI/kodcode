from solution import *

from solution import TreeNode, vertical_order_traversal

# Example tree
#     3
#    / \
#   9  20
#     /  \
#    15   7
node_3 = TreeNode(3)
node_9 = TreeNode(9)
node_20 = TreeNode(20)
node_15 = TreeNode(15)
node_7 = TreeNode(7)

node_3.left = node_9
node_3.right = node_20
node_20.left = node_15
node_20.right = node_7

def test_vertical_order_traversal():
    assert vertical_order_traversal(node_3) == [[9], [3, 15], [20], [7]]

# Tree with a single node
single_node = TreeNode(1)
def test_single_node():
    assert vertical_order_traversal(single_node) == [[1]]

# Tree with no nodes
def test_no_nodes():
    assert vertical_order_traversal(None) == []

# Tree with multiple nodes
#     10
#    /  \
#   3    5
#  / \
# 2   1
node_10 = TreeNode(10)
node_3 = TreeNode(3)
node_5 = TreeNode(5)
node_2 = TreeNode(2)
node_1 = TreeNode(1)

node_10.left = node_3
node_10.right = node_5
node_3.left = node_2
node_3.right = node_1
def test_multiple_nodes():
    assert vertical_order_traversal(node_10) == [[2], [3], [10], [5, 1]]