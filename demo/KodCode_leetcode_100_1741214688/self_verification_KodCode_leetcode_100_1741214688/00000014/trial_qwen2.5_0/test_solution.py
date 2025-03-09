from solution import *

from solution import TreeNode, sum_odd_parent_nodes

def test_sum_odd_parent_nodes():
    # Tree:        1
    #              / \
    #             2   3
    #            / \   \
    #           4   5   6
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_2 = TreeNode(2, node_4, node_5)
    node_3 = TreeNode(3, None, node_6)
    root = TreeNode(1, node_2, node_3)
    assert sum_odd_parent_nodes(root) == 12  # 4 + 5 + 3 (since 2 and 1 are odd, and 5, 3 are children of odd nodes)

def test_sum_odd_one_branch():
    # Tree:        1
    #              / \
    #             2   3
    #            /     \
    #           4       5
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_2 = TreeNode(2, node_4, None)
    node_3 = TreeNode(3, None, node_5)
    root = TreeNode(1, node_2, node_3)
    assert sum_odd_parent_nodes(root) == 6  # 4 (since 2 is odd, and 4 is child of odd node)

def test_sum_odd_multiple_branches():
    # Tree:        1
    #              / \
    #             2   3
    #            / \   \
    #           4   5   6
    #          / \
    #         7   8
    node_7 = TreeNode(7)
    node_8 = TreeNode(8)
    node_4 = TreeNode(4, node_7, node_8)
    node_2 = TreeNode(2, node_4, None)
    node_3 = TreeNode(3, None, node_6)
    root = TreeNode(1, node_2, node_3)
    assert sum_odd_parent_nodes(root) == 18  # 8 + 7 + 5 + 3 (since 2, 4, 1 are odd, and 7, 8, 5, 3 are children of odd nodes)

def test_sum_no_odd_node():
    # Tree:        2
    #              / \
    #             4   6
    #            / \
    #           8   10
    node_8 = TreeNode(8)
    node_10 = TreeNode(10)
    node_4 = TreeNode(4, node_8, node_10)
    node_2 = TreeNode(2, node_4, None)
    root = TreeNode(2, node_2, None)
    assert sum_odd_parent_nodes(root) == 0