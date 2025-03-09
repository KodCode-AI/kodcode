from solution import *

def test_min_balance_factor():
    # Tree:
    #     1
    #    / \
    #   2   3
    #  /
    # 4
    tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    assert min_balance_factor(tree) == 0

    # Tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert min_balance_factor(tree) == -1

    # Tree:
    #     1
    #    /
    #   2
    #  /
    # 4
    tree = TreeNode(1, TreeNode(2, TreeNode(4)))
    assert min_balance_factor(tree) == -1

    # Tree:
    #     1
    #    / \
    #   2   3
    #  /     \
    # 4       5
    tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
    assert min_balance_factor(tree) == -2

    # Tree:
    #     1
    #    /
    #   2
    #  / \
    # 4   5
    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)))
    assert min_balance_factor(tree) == 1

    # Tree is empty
    assert min_balance_factor(None) == 0

    # Single node tree
    tree = TreeNode(1)
    assert min_balance_factor(tree) == 0