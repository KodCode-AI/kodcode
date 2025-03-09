from solution import *

from solution import TreeNode, sum_odd_parent_nodes

def test_sum_odd_parent_nodes():
    # Creating a simple tree
    #       5
    #      / \
    #     3   7
    node5 = TreeNode(5)
    node3 = TreeNode(3)
    node7 = TreeNode(7)
    node5.left = node3
    node5.right = node7
    
    assert sum_odd_parent_nodes(node5) == 3  # Only node3 has an odd parent (node5)

def test_sum_odd_parent_nodes_no_affected_nodes():
    # Creating a simple tree
    #       2
    #      / \
    #     4   6
    node2 = TreeNode(2)
    node4 = TreeNode(4)
    node6 = TreeNode(6)
    node2.left = node4
    node2.right = node6
    
    assert sum_odd_parent_nodes(node2) == 0  # No nodes have an odd parent

def test_sum_odd_parent_nodes Complex_case():
    # Creating a tree
    #       8
    #      / \
    #     3   5
    #    / \ / \
    #   2  9 7  2
    node8 = TreeNode(8)
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    node8.left = node3
    node8.right = node5
    node2 = TreeNode(2)
    node9 = TreeNode(9)
    node7 = TreeNode(7)
    node22 = TreeNode(2)
    node3.left = node2
    node3.right = node9
    node5.left = node7
    node5.right = node22
    
    assert sum_odd_parent_nodes(node8) == 11  # Nodes 9 and 7 have odd parent (5) and (3) respectively

def test_sum_odd_parent_nodes_single_node():
    # Creating a tree with a single node
    node1 = TreeNode(1)
    assert sum_odd_parent_nodes(node1) == 0  # No parent for the single node