from solution import *

def create_tree(*values):
    def build_tree(nodes, index=1):
        if not nodes or index > len(nodes) or not nodes[index-1]:
            return None
        root = TreeNode(nodes[index-1])
        root.left = build_tree(nodes, 2*index)
        root.right = build_tree(nodes, 2*index+1)
        return root
    return build_tree(values)

from solution import sum_of_left_leaves

def test_sum_of_left_leaves():
    assert sum_of_left_leaves(create_tree(3, 9, 20, None, None, 15, 7)) == 24

def test_sum_of_left_leaves_with_no_left_leaf():
    assert sum_of_left_leaves(create_tree(1, 2, 3, 4, 5)) == 0

def test_sum_of_left_leaves_single_node():
    assert sum_of_left_leaves(create_tree(1)) == 0

def test_sum_of_left_leaves_complex_tree():
    assert sum_of_left_leaves(create_tree(1, 2, 3, 4, 5, 6, 7, None, None, 8)) == 22

def test_sum_of_left_leaves_empty_tree():
    assert sum_of_left_leaves(None) == 0