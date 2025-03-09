from solution import *

from solution import max_depth, TreeNode

def create_tree(*values):
    if not values:
        return None
    nodes = [None if val is None else TreeNode(val) for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def test_max_depth():
    assert max_depth(None) == 0

def test_max_depth_single_node():
    root = create_tree(1)
    assert max_depth(root) == 1

def test_max_depth_complete_binary_tree():
    #         1
    #        / \
    #       2   3
    #      / \ / \
    #     4  5 6  7
    #    / \
    #   8   9
    root = create_tree(1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert max_depth(root) == 4

def test_max_depth_skewed_tree():
    #         1
    #          \
    #           2
    #            \
    #             3
    root = create_tree(1, None, 2, None, None, None, 3)
    assert max_depth(root) == 3

def test_max_depth_unbalanced_tree():
    #         1
    #        /
    #       2
    #      /
    #     3
    #    /
    #   4
    root = create_tree(1, 2, None, 3, None, None, 4)
    assert max_depth(root) == 4